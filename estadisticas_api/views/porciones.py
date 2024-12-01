from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from estadisticas_api.models import Seguimiento_porciones
from estadisticas_api.serializers import seguimiento_porcionesSerializers


class SeguimientoPorcionesView(APIView):
    def get(self, request):
        seguimientos = Seguimiento_porciones.objects.all().order_by('-fecha')
        serializer = seguimiento_porcionesSerializers(seguimientos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = seguimiento_porcionesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
