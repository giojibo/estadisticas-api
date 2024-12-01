from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from estadisticas_api.models import Seguimiento_calorico
from estadisticas_api.serializers import seguimiento_caloricoSerializers

class SeguimientoCaloricoView(APIView):
    def get(self, request):
        seguimientos = Seguimiento_calorico.objects.all().order_by('-fecha')
        serializer = seguimiento_caloricoSerializers(seguimientos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = seguimiento_caloricoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
