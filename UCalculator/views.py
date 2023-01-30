from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Material, Composite, Component
from django.contrib.auth.models import User
from .forms import NewComponentForm, ClearForm

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
    composites = Composite.objects.filter(user=request.user).all()
    components = Component.objects.filter(user=request.user).filter(active=True).all()
    user = request.user
    
    clear_form = ClearForm()
    
    uVal = 'N/A'

    if components:
        rList = [component.calcR() for component in components]
        rSum = sum(rList)
        uVal = (1 / (0.13 + rSum + 0.04))


    if request.method == 'POST':
        
        if 'add_material' in request.POST: 
            form = NewComponentForm(request.POST)
            if form.is_valid():
                component = form.save(commit=False)
                component.user = user
                component.save()
                return redirect('calculator')
        
        if 'clear_material_view' in request.POST:
            for component in components:
                print(component)
                if component.composite:
                    component.active = False
                else:
                    component.delete()
            components = Component.objects.filter(user=request.user).filter(active=True).all()
            uVal = 'N/A'
    
    component_form = NewComponentForm()
    context = {
        'materials': materials,
        'composites': composites,
        'components': components,
        'component_form': component_form,
        'clear_form': clear_form,
        'uVal': uVal
    }
        
    return render(request, 'calculator.html', context)