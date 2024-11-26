from rest_framework import serializers
from models import Seguimiento_calorico, Seguimiento_porciones, PesoMensual

class seguimiento_caloricoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_calorico
        fields = '__all__'

class seguimiento_porcionesSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Seguimiento_porciones
        fiedls = '__all__'

class pesoMensualSerializers(serializers.ModelSerializer):
    class Meta:
        model = PesoMensual
        fields = '__all__'