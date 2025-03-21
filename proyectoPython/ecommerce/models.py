from django.db import models

# Create your models here.
#class ProductModel(models.Model):
#    title = models.TextField()
#    price = models.FloatField()      

class Ingreso(models.Model):
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion