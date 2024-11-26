from django.urls import path
from estadisticas_api.views import calorias

urlpatterns = [
    path('calorias/', calorias.SeguimientoCaloricoView.as_view(), name='calorias'),
]
