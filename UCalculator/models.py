from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=30, unique=True)
    thermal_conductivity = models.FloatField(max_length=10)
    def __str__(self):
        return self.name

class Composite(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    thickness = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    composite = models.ForeignKey(Composite, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def calcR(self):
        return ((self.thickness * 0.001) / self.material.thermal_conductivity)
    
    def displayR(self):
        return round((self.thickness * 0.001) / self.material.thermal_conductivity, 1)

    def __str__(self):
        return self.material.name + ' (' + str(self.thickness) + 'mm)'

