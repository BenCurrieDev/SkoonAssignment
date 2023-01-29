from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Material, Composite, Component
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    materials = Material.objects.all()
    context = { 'materials': materials }
    return render(request, 'home.html', context)

def calculator(request):
    materials = Material.objects.all()
    composites = Composite.objects.all()
    components = Component.objects.all()
    context = {
        'materials': materials,
        'composites': composites,
        'components': components,
    }

    if request.method == 'POST':
        material = Material.objects.get(pk=request.POST['material'])
        thickness = int(request.POST['thickness'])

        user = User.objects.first() # NEED TO REPLACE WITH ACTUAL USER

        component = Component.objects.create(
            material=material,
            thickness=thickness,
            user=user
        )

        return redirect('calculator')

    return render(request, 'calculator.html', context)