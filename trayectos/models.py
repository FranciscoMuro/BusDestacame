from django.db import models
from choferes.models import Chofer

# Create your models here.
class Trayecto(models.Model):
    trayectoId = models.AutoField(primary_key=True)
    choferId = models.ForeignKey(Chofer, verbose_name="Chofer del autobus", on_delete=models.CASCADE)
    origen = models.CharField("ubicacion de partida del viaje", max_length=50)
    destino = models.CharField("ubicacion de llegada del viaje", max_length=50)
    fecha_hora_salida = models.DateField()
