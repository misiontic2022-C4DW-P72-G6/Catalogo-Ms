from rest_framework import generics
from cata1App.models.habitacion import Habitacion
from cata1App.serializers.habitacionSerializer import habitacionSerializer

class habitacionDetailView(generics.RetrieveAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = habitacionSerializer