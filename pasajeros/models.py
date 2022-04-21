from pyexpat import model
from django.db import models
from autobuses.models import Autobus

# Create your models here.
class Pasajero(models.Model):
    pasajeroId = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre del pasajero", max_length=50)
    autobus = models.ForeignKey(Autobus, verbose_name="Autobus asignado", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre