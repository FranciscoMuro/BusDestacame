from django.db import models

# Create your models here.
class Trayecto(models.Model):
    trayectoId = models.AutoField(primary_key=True)
    origen = models.CharField("ubicacion de partida del viaje", max_length=50)
    destino = models.CharField("ubicacion de llegada del viaje", max_length=50)


    def __str__(self):
        return self.origen+'-'+self.destino