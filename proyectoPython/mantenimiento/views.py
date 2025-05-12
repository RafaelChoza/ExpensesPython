from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import MantenimientoForm, TecnicoForm, AreaForm
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Mantenimiento, Tecnico, Area

def mantenimiento_view(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mantenimiento/mantenimientos-list')  # Redirige a una página de éxito
    else:
        form = MantenimientoForm()

    return render(request, 'mantenimiento_form.html', {'form': form})

def tecnico_view(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mantenimiento/tecnicos-list/')
    else:
        form = TecnicoForm()

    return render(request, "tecnico_form.html", {'form': form})

def area_view(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mantenimiento/areas-list/')
    else:
        form = AreaForm()

    return render(request, "areas_form.html", {'form': form})

class MantenimientosList(ListView):
    model = Mantenimiento
    template_name = 'mantenimientos_list.html'
    context_object_name = 'mantenimientos'

class TecnicosList(ListView):
    model = Tecnico
    template_name = 'tecnicos_list.html'
    context_object_name = 'tecnicos'

class AreasList(ListView):
    model = Area
    template_name = 'areas_list.html'
    context_object_name = 'areas'

class TecnicoUpdateView(UpdateView):
    model = Tecnico
    fields = ['nombreTecnico', 'apellidoTecnico']
    template_name = 'tecnico_form.html'
    success_url = '/mantenimiento/tecnicos-list/'

class AreaUpdateView(UpdateView):
    model = Area
    fields = ['nombreArea']
    template_name = 'areas_form.html'
    success_url = '/mantenimiento/areas-list/'

class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    fields = [
        'requestorName', 'requestorLastName', 'creationDateTime', 'idMachine', 'area', 
        'machineStopped', 'attentionRequired', 'problemDescription', 'receptionDateTime', 
        'personnelAsigned', 'programmedDate', 'problemObservations', 'problemCuaseSolution', 
        'scrapEquipment', 'needCalibration', 'problemCuaseSolutionDate', 'usedParts1', 
        'partNumber1', 'description1', 'usedParts2', 'partNumber2', 'description2', 
        'usedParts3', 'partNumber3', 'description3', 'coversInstalled', 'interlocksTested', 
        'gardsInstalled', 'electricalConexions', 'visualRevision', 'areaCleaned', 
        'airGasWaterConexion', 'tagsInEquipment', 'finalRevisionComments', 'closeDate'
    ]
    template_name = 'mantenimiento_form.html'
    success_url = '/mantenimiento'

class TecnicoDeleteView(DeleteView):
    model = Tecnico
    template_name = 'tecnico_confirmar_eliminar.html'
    success_url = reverse_lazy('tecnicosList')

class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'area_confirmar_eliminar.html'
    success_url =  reverse_lazy('areasList')

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento_confirmar_eliminar.html'
    success_url = reverse_lazy('mantenimientosList')