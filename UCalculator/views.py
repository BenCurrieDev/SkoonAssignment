from django.shortcuts import render
from django.http import HttpResponse
from .models import Material, Composite, Component

# Create your views here.
def home(request):
    materials = Material.objects.all()
    material_names = [material.name for material in materials]
    response_html = '<br>'.join(material_names)
    return HttpResponse(response_html)