from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Material, Composite, Component
from django.contrib.auth.models import User
from .forms import NewComponentForm

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    materials = Material.objects.all()
    context = { 'materials': materials }
    return render(request, 'home.html', context)

@login_required
def calculator(request):
    materials = Material.objects.all()
    composites = Composite.objects.all()
    components = Component.objects.all()
    user = request.user

    if request.method == 'POST':
        form = NewComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.user = user
            component.save()
            return redirect('calculator')

    else:
        form = NewComponentForm()
        context = {
            'materials': materials,
            'composites': composites,
            'components': components,
            'form': form
        }
        
    return render(request, 'calculator.html', context)