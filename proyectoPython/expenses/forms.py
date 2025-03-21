from django import forms
from .models import Ingreso, Gasto

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['descripcion', 'cantidad', 'fecha', 'categoria']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'cantidad', 'fecha', 'categoria']