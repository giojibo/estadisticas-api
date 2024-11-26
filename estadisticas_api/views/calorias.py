from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Seguimiento_calorico
from serializers import SeguimientoCaloricoSerializer

class SeguimientoCaloricoView(APIView):
    def get(self, request):
        seguimientos = Seguimiento_calorico.objects.all().order_by('-fecha')
        serializer = SeguimientoCaloricoSerializer(seguimientos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SeguimientoCaloricoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
