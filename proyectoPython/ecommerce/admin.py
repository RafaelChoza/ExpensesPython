from django.contrib import admin
#from .models import ProductModel
from .models import Ingreso, Gasto
# Register your models here.
admin.site.register(Gasto)
admin.site.register(Ingreso)