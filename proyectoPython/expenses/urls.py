from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_ingreso/', views.agregar_ingreso, name='agregar_ingreso'),
    path('agregar_gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('editar_ingreso/<int:pk>/', views.editar_ingreso, name='editar_ingreso'),
    path('editar_gasto/<int:pk>/', views.editar_gasto, name='editar_gasto'),
    path('eliminar_ingreso/<int:pk>/', views.eliminar_ingreso, name='eliminar_ingreso'),
    path('eliminar_gasto/<int:pk>/', views.eliminar_gasto, name='eliminar_gasto'),
]