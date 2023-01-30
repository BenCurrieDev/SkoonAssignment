from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Material, Composite, Component
from django.contrib.auth.models import User
from .forms import NewComponentForm, ClearForm, SaveForm

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    materials = Material.objects.all()
    composites = Composite.objects.filter(user=request.user).all()
    context = { 
        'materials': materials,
        'composites': composites
         }
    return render(request, 'home.html', context)

@login_required
def calculator(request):
    materials = Material.objects.all()
    composites = Composite.objects.filter(user=request.user).filter(active=True).all()
    if composites:
        active_composite = composites[0]
    else:
        active_composite = ''
    components = Component.objects.filter(user=request.user).filter(active=True).all()
    user = request.user
    clear_form = ClearForm()
    uVal = 'N/A'
    if components:
        rList = [component.calcR() for component in components]
        rSum = sum(rList)
        uVal = round(1 / (0.13 + rSum + 0.04), 2)


    if request.method == 'POST':
        
        if 'add_material' in request.POST: 
            form = NewComponentForm(request.POST)
            if form.is_valid():
                component = form.save(commit=False)
                component.user = user
                component.save()
                return redirect('calculator')
        
        if 'clear_material_view' in request.POST:
            print('Clearing...')
            for component in components:
                if component.composite:
                    component.active = False
                    component.save()
                else:
                    component.delete()
            if composites:
                active_composite.active = False
                active_composite.save()
            return redirect('calculator')
        
        if 'save_composite' in request.POST:
            print('Saving...')
            if components:
                form = SaveForm(request.POST)
                if form.is_valid():
                    print('Save was valid')
                    active_composite.active = False
                    active_composite.save()
                    composite = form.save(commit=False)
                    composite.user = user
                    composite.save()
                    print('Saved composite. Attempting to update component relations...')
                    for component in components:
                        component.composite = composite
                        component.save()
                    
                    return redirect('calculator')

    component_form = NewComponentForm()
    save_form = SaveForm()

    context = {
        'materials': materials,
        'composites': composites,
        'active_composite': active_composite,
        'components': components,
        'component_form': component_form,
        'clear_form': clear_form,
        'save_form': save_form,
        'uVal': uVal
    }
        
    return render(request, 'calculator.html', context)