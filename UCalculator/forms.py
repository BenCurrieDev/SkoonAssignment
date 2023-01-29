from django import forms
from .models import Material, Component, Composite

class NewComponentForm(forms.ModelForm):

    class Meta:
        model = Component
        fields = ['material', 'thickness']