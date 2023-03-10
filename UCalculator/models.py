from django.db import models
from django.contrib.auth.models import User
from .constants import Rsi, Rse


class Material(models.Model):
    name = models.CharField(max_length=30, unique=True)
    K_value = models.FloatField()
    color = models.CharField(max_length=30, default="grey")

    def __str__(self):
        return self.name


class Composite(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def total_depth(self):
        components = self.component_set.all()
        depths = [component.depth for component in components]
        return sum(depths)

    def U_value_2dp(self):
        components = self.component_set.all()
        if components:
            R_values = [component.R_value() for component in components]
            R_total = Rsi + sum(R_values) + Rse
            return round(1 / R_total, 2)
        else:
            return 'N/A'

    def __str__(self):
        return self.name


class Component(models.Model):
    depth = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    composite = models.ForeignKey(
        Composite, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def R_value(self):
        return ((self.depth * 0.001) / self.material.K_value)

    def R_value_2dp(self):
        return round((self.depth * 0.001) / self.material.K_value, 2)

    def __str__(self):
        return self.material.name + ' (' + str(self.depth) + 'mm)'
