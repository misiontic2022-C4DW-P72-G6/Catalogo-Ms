from rest_framework import serializers
from cata1App.models.habitacion import Habitacion

class habitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['idHabitacion','tipoHabitacion','capacidadHabitacion','costoHabitacion','descripcionHabitacion', 'idHotel']
