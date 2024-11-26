from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from models import PesoMensual
from serializers import pesoMensualSerializers

class PesoMensualListCreateAPIView(APIView):
    
    def get(self, request):
        registros = PesoMensual.objects.all()
        serializer = pesoMensualSerializers(registros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = pesoMensualSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PesoMensualRetrieveUpdateDeleteAPIView(APIView):
   
    def get_object(self, pk):
        try:
            return PesoMensual.objects.get(pk=pk)
        except PesoMensual.DoesNotExist:
            return None

    def get(self, request, pk):
        registro = self.get_object(pk)
        if registro:
            serializer = pesoMensualSerializers(registro)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        registro = self.get_object(pk)
        if registro:
            serializer = pesoMensualSerializers(registro, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        registro = self.get_object(pk)
        if registro:
            registro.delete()
            return Response({"message": "Registro eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)