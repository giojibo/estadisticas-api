from django.db import models

# Create your models here.

class Seguimiento_calorico(models.Model):
    paciente = models.CharField(max_length=100)  
    calorias_recomendadas = models.PositiveIntegerField()
    calorias_consumidas = models.PositiveIntegerField()    
    calorias_excedentes = models.PositiveIntegerField(default=0)  
    fecha = models.DateField(auto_now_add=True)      

    def calorias_restantes(self):
        # Calcula las calorías restantes automáticamente
        return max(self.calorias_recomendadas - self.calorias_consumidas, 0)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
    
class Seguimiento_porciones(models.Model):
    paciente = models.CharField(max_length=100)  
    porciones_recomendadas = models.PositiveIntegerField()  
    porciones_consumidas = models.PositiveIntegerField()
    porciones_excedentes = models.PositiveIntegerField(default=0)  
    fecha = models.DateField(auto_now_add=True)             

    @property
    def porciones_faltantes(self):
        # Calcula las porciones faltantes automáticamente
        return max(self.porciones_recomendadas - self.porciones_consumidas, 0)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
    
class PesoMensual(models.Model):
    paciente = models.CharField(max_length=100)  
    mes = models.CharField(max_length=20)        
    anio = models.PositiveIntegerField()        
    peso_inicial = models.FloatField()           
    calorias_recomendadas = models.PositiveIntegerField()  
    calorias_consumidas = models.PositiveIntegerField()    
    calorias_excedentes = models.PositiveIntegerField(default=0)  
    peso_calculado = models.FloatField(blank=True, null=True)     

    def calcular_peso(self):
        deficit = self.calorias_recomendadas - self.calorias_consumidas
        peso_perdido = deficit / 7700  
        return round(self.peso_inicial + self.calorias_excedentes / 7700 - peso_perdido, 2)

    def save(self, *args, **kwargs):
        if self.peso_calculado is None:
            self.peso_calculado = self.calcular_peso()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.paciente} - {self.mes} {self.anio}"
    
    