from django.contrib import admin
from .models import Mantenimiento, Tecnico, Area

# Register your models here.
admin.site.register(Mantenimiento)
admin.site.register(Tecnico)
admin.site.register(Area)