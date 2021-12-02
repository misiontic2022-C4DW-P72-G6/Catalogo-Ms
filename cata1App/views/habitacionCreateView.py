from rest_framework import status, views
from rest_framework.response import Response
from cata1App.serializers import habitacionSerializer

class habitacionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = habitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(habitacionSerializer.validated_data, status=status.HTTP_201_CREATED)