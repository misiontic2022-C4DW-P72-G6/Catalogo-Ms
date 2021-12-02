from rest_framework import generics
from cata1App.models.catalogo import catalogo
from cata1App.serializers.catalogoSerializer import catalogoSerializer

class catalogoDetailView(generics.RetrieveAPIView):
    queryset = catalogo.objects.all()
    serializer_class = catalogoSerializer