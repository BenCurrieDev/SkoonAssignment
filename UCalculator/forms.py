from django import forms
from .models import Material, Component, Composite

class NewComponentForm(forms.ModelForm):
    add_material = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Component
        fields = ['material', 'thickness']

class ClearForm(forms.Form):
    clear_material_view = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class SaveForm(forms.Form):
    save_composite = forms.BooleanField(widget=forms.HiddenInput, initial=True)