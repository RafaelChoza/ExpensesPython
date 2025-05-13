from django import forms
from .models import Mantenimiento, Tecnico, Area, ParteUsada
from django.forms import modelformset_factory

ParteUsadaFormSet = modelformset_factory(ParteUsada, fields=("cantidad", "numero_parte", "descripcion"), extra=1)

class MantenimientoForm(forms.ModelForm):
    personnelAsigned = forms.ModelChoiceField(
        queryset= Tecnico.objects.all(),
        label="Tecnico Asignado",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    area =forms.ModelChoiceField(
        queryset=Area.objects.all(),
        label = 'Area',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    tech = forms.ModelChoiceField(
        queryset=Tecnico.objects.all(),
        label="Nombre del Tecnico",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    receptionDateTime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    programmedDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    problemCuaseSolutionDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    closeDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Mantenimiento
        exclude = ['creationDateTime']  # Excluimos el campo no editable


class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombreTecnico', 'apellidoTecnico']
        widgets = {
            'nombreTecnico': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoTecnico': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombreArea']
        widgets = {
            'nombreArea': forms.TextInput(attrs={'class': 'form-ontrol'})
        }