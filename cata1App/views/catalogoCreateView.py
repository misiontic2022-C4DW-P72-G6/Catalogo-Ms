from rest_framework import status, views
from rest_framework.response import Response
from cata1App.serializers import catalogoSerializer

class catalogoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = catalogoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(catalogoSerializer.validated_data, status=status.HTTP_201_CREATED)