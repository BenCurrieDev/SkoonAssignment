from django.shortcuts import render
from django.http import HttpResponse
from .models import Material, Composite, Component

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
        material = request.post['material']
        thickness = request.post['thickness']
        
    return render(request, 'calculator.html', context)