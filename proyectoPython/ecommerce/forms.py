from django import forms

#from .models import ProductModel

from .models import Ingreso, Gasto
from datetime import date, timedelta

#class ProductModelForm(forms.ModelForm):
#    class Meta:
#        model = ProductModel
#        fields = [
#            "title",
#            "price"
#        ]

# Define las opciones para el campo 'categoria'
CATEGORIAS_INGRESOS = [
    ('salario', 'Salario'),
    ('vales', 'Vales'),
    ('aguinaldo', 'Aguinaldo'),
    ('regalo', 'Regalo'),
    ('bono', 'Bono'),
    ('otro', 'Otro'),
]

CATEGORIAS_GASTOS = [
    ('comida', 'Comida'),
    ('casa', 'Casa'),
    ('deportes', 'Deportes'),
    ('ropa', 'Ropa'),
    ('diversion', 'Diversión'),
    ('educacion', 'Educación'),
    ('automovil', 'Automovil'),
    ('salud', 'Salud'),
    ('transporte', 'Transporte'),
    ('otro', 'Otro'),
]

class IngresoForm(forms.ModelForm):
    categoria = forms.ChoiceField(choices=CATEGORIAS_INGRESOS)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Ingreso
        fields = ['descripcion', 'cantidad', 'fecha', 'categoria']

class GastoForm(forms.ModelForm):
    categoria = forms.ChoiceField(choices=CATEGORIAS_GASTOS)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Gasto
        fields = ['descripcion', 'cantidad', 'fecha', 'categoria']