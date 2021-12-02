from django.db import models
from django.db.models.base import Model

class catalogo(Model):
    idHotel = models.AutoField(primary_key=True)
    Nombre = models.CharField('nombre',max_length=60, null=False)
    Ubicacion = models.CharField('ubicacion',max_length=60, null=False)
    Calificacion = models.IntegerField(default=0)  
    Direccion = models.CharField('direccion',max_length=60, null=False)
    Descripcion = models.CharField('descripcion',max_length=60, null=False)
    Correo = models.CharField('correo',max_length=60, null=False)
    
    