from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
#from .models import ProductModel
#from .forms import ProductModelForm

from django.shortcuts import render, redirect
from .models import Ingreso, Gasto
from .forms import IngresoForm, GastoForm

# Create your views here.

#def product_model_delete_view(request, product_id):
#    instance = get_object_or_404(ProductModel, id=product_id)
#    if request.method == "POST":
#        instance.delete()
#        HttpResponseRedirect("/")
#        messages.success(request, "Producto eliminado")
#        return HttpResponseRedirect("/")
#    context = {
#        "product": instance
#    }
#    template = "ecommerce/delete-view.html"
#    return render(request, template, context)
#
#def product_model_update_view(request, product_id=None):
#    instance = get_object_or_404(ProductModel, id=product_id)
#    form = ProductModelForm(request.POST or None, instance=instance)
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        messages.success(request, "Producto actualizado con éxito")
#        return HttpResponseRedirect("/{product_id}".format(product_id=instance.id))
#    context = {
#        "form": form
#    }
#    template = "ecommerce/update-view.html"
#    return render(request, template, context)
#
#def product_model_create_view(request):
#    form = ProductModelForm(request.POST or None)
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        messages.success(request, "Producto creado con éxito")
#        return HttpResponseRedirect("/{product_id}".format(product_id=instance.id))
#    context = {
#        "form": form
#    }
#    template = "ecommerce/create-view.html"
#    return render(request, template, context)
#
#def product_model_detail_view(request, product_id):
#    instance = ProductModel.objects.filter(id=product_id).first()  # Busca el producto; devuelve None si no lo encuentra.
#    if instance:
#        context = {
#            "product": instance
#        }
#        template = "ecommerce/detail-view.html"
#        return render(request, template, context)
#    else:
#        # Renderizar una plantilla diferente si no se encuentra el producto
#        template = "ecommerce/product-not-found.html"
#        return render(request, template, {"product_id": product_id})

    

#@login_required
#def product_model_list_view(request):
#    query = request.GET.get("q", None)
#    queryset = ProductModel.objects.all()
#    if query is not None:
#        queryset = queryset.filter(
#            Q(title__contains=query) |
#            Q(price__contains=query) 
#        )
#    template = "ecommerce/list-view.html"
#    context = {
#        "products": queryset
#    }

#    if request.user.is_authenticated:
#        template = "ecommerce/list-view.html"
#    else:
#        template = "ecommerce/list-view-public.html"
#    return render(request, template, context)

#@login_required
#def login_required_view(request):
#    print(request.user)
#    queryset = ProductModel.objects.all()
#    template = "ecommerce/list-view.html"
#    context = {
#        "products": queryset
#    }

#    if request.user.is_authenticated:
#        template = "ecommerce/list-view.html"
#    else:
#        template = "ecommerce/list-view-public.html"
#
#    return render(request, template, context)



def index(request):
    query = request.GET.get('q')
    if query:
        ingresos = Ingreso.objects.filter(
            Q(descripcion__icontains=query) | 
            Q(categoria__icontains=query)
        )
        gastos = Gasto.objects.filter(
            Q(descripcion__icontains=query) | 
            Q(categoria__icontains=query)
        )
    else:
        ingresos = Ingreso.objects.all()
        gastos = Gasto.objects.all()

    total_ingresos = sum(ingreso.cantidad for ingreso in ingresos)
    total_gastos = sum(gasto.cantidad for gasto in gastos)
    balance = total_ingresos - total_gastos

    context = {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'ingresos': ingresos, 
        'gastos': gastos, 
        'balance': balance
    }
    return render(request, 'ecommerce/index.html', context)

def agregar_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IngresoForm()
    return render(request, 'ecommerce/agregar_ingreso.html', {'form': form})

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GastoForm()
    return render(request, 'ecommerce/agregar_gasto.html', {'form': form})

def editar_ingreso(request, pk):
    ingreso = Ingreso.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'ecommerce/editar_ingreso.html', {'form': form})

def editar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'ecommerce/editar_gasto.html', {'form': form})

def eliminar_ingreso(request, pk):
    ingreso = Ingreso.objects.get(pk=pk)
    ingreso.delete()
    return redirect('index')

def eliminar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    gasto.delete()
    return redirect('index')

def eliminar_todo(request):
    if request.method == 'POST':
        Ingreso.objects.all().delete()
        Gasto.objects.all().delete()
        return redirect('index')
    return render(request, 'ecommerce/eliminar_todo.html')