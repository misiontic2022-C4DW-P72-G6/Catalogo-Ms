from rest_framework import serializers
from cata1App.models.catalogo import catalogo


class catalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo
        fields = ['idHotel','Nombre','Ubicacion','Calificacion','Direccion','Descripcion','Correo']