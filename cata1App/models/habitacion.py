from django.db import models
from django.db.models.base import Model
from .catalogo import catalogo

class Habitacion(Model):
    idHabitacion= models.BigAutoField(primary_key=True)
    tipoHabitacion= models.CharField('tipoHabitacion',max_length=30, unique=False)
    capacidadHabitacion= models.IntegerField(default=0)
    costoHabitacion= models.IntegerField(default=0)
    descripcionHabitacion=models.CharField('descripcionHabitacion',max_length=300, unique=False)
    idHotel= models.ForeignKey(catalogo,related_name='idCatalogo',on_delete=models.CASCADE)
    
   