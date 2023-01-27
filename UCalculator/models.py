from django.db import models

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=30, unique=True)
    thermal_conductivity = models.FloatField(max_length=10)

class Composite(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Component(models.Model):
    thickness = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    composite = models.ForeignKey(Composite, on_delete=models.CASCADE)