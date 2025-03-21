from django.shortcuts import render, redirect
from .models import Ingreso, Gasto
from .forms import IngresoForm, GastoForm

def index(request):
    ingresos = Ingreso.objects.all()
    gastos = Gasto.objects.all()
    balance = sum(ingreso.cantidad for ingreso in ingresos) - sum(gasto.cantidad for gasto in gastos)
    return render(request, 'finanzas/index.html', {'ingresos': ingresos, 'gastos': gastos, 'balance': balance})

def agregar_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IngresoForm()
    return render(request, 'finanzas/agregar_ingreso.html', {'form': form})

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GastoForm()
    return render(request, 'finanzas/agregar_gasto.html', {'form': form})

def editar_ingreso(request, pk):
    ingreso = Ingreso.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'finanzas/editar_ingreso.html', {'form': form})

def editar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'finanzas/editar_gasto.html', {'form': form})

def eliminar_ingreso(request, pk):
    ingreso = Ingreso.objects.get(pk=pk)
    ingreso.delete()
    return redirect('index')

def eliminar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    gasto.delete()
    return redirect('index')