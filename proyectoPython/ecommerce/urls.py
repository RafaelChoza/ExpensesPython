from django.urls import path
from ecommerce import views

#urlpatterns = [
#    path('', views.product_model_list_view, name="list"),
#    path("<int:product_id>", views.product_model_detail_view, name="detail"),
#    path("create", views.product_model_create_view, name="create"),
#    path("<int:product_id>/edit/", views.product_model_update_view, name="update"),
#    path("<int:product_id>/delete/", views.product_model_delete_view, name="delete"),
#]

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_ingreso/', views.agregar_ingreso, name='agregar_ingreso'),
    path('agregar_gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('editar_ingreso/<int:pk>/', views.editar_ingreso, name='editar_ingreso'),
    path('editar_gasto/<int:pk>/', views.editar_gasto, name='editar_gasto'),
    path('eliminar_ingreso/<int:pk>/', views.eliminar_ingreso, name='eliminar_ingreso'),
    path('eliminar_gasto/<int:pk>/', views.eliminar_gasto, name='eliminar_gasto'),
    path('eliminar_todo/', views.eliminar_todo, name='eliminar_todo'),
]