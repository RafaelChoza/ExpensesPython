from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    requestorName = models.CharField(max_length=100)
    requestorLastName = models.CharField(max_length=100)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    idMachine = models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    machineStopped= models.BooleanField()
    attentionRequired = models.BooleanField()
    problemDescription = models.TextField(max_length=400)
    receptionDateTime = models.DateTimeField()
    personnelAsigned = models.CharField(max_length=100)
    programmedDate = models.DateField()
    problemObservations = models.TextField(max_length=400)
    problemCuaseSolution = models.TextField(max_length=400)
    scrapEquipment = models.BooleanField()
    needCalibration = models.BooleanField()
    problemCuaseSolutionDate = models.DateField()
    resportedDate = models.DateField(null=True, blank=True)
    tech = models.CharField(max_length=100)
    timeServiceStart = models.DateTimeField(null=True, blank=True)
    timeServiceEnd = models.DateTimeField(null=True, blank=True)
    coversInstalled = models.BooleanField()
    interlocksTested = models.BooleanField()
    gardsInstalled = models.BooleanField()
    electricalConexions = models.BooleanField()
    visualRevision = models.BooleanField()
    areaCleaned = models.BooleanField()
    airGasWaterConexion = models.BooleanField()
    tagsInEquipment = models.BooleanField()
    finalRevisionComments = models.TextField(max_length=400)
    closeDate = models.DateField()

    def __str__(self):
        return ", ".join([field.verbose_name for field in self._meta.fields])
    
class Tecnico(models.Model):
    nombreTecnico = models.CharField(max_length=100)
    apellidoTecnico = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombreTecnico} {self.apellidoTecnico}"

class Area(models.Model):
    nombreArea = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombreArea}"
    
class ParteUsada(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE, related_name="partes")
    cantidad = models.CharField(max_length=255)
    numero_parte = models.CharField(max_length=100)
    descripcion = models.TextField()