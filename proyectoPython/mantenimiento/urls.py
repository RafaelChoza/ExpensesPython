from django.urls import path
from . import views

urlpatterns = [
    path('', views.mantenimiento_view, name='mantenimientos'),
    path('tecnicos/', views.tecnico_view, name='tecnicos'),
    path('areas/', views.area_view, name='areas'),
    path('mantenimientos-list/', views.MantenimientosList.as_view(), name='mantenimientosList'),
    path('tecnicos-list/', views.TecnicosList.as_view(), name='tecnicosList'),
    path('areas-list/', views.AreasList.as_view(), name='areasList'),
    path('tecnicos/edit/<int:pk>/', views.TecnicoUpdateView.as_view(), name='editTecnico'),
    path('areas/edit/<int:pk>/', views.AreaUpdateView.as_view(), name='editArea'),
    path('mantenimientos/edit/<int:pk>/', views.MantenimientoUpdateView.as_view(), name='editMantenimiento'),
]