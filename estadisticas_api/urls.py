from django.urls import path
from estadisticas_api.views import calorias, porciones, pesoMensual

urlpatterns = [
    path('calorias/', calorias.SeguimientoCaloricoView.as_view(), name='calorias'),
    path('porciones/', porciones.SeguimientoPorcionesView.as_view(), name='porciones'),
    path('peso-mensual/', pesoMensual.PesoMensualListCreateAPIView.as_view(), name='peso mensual')
]
