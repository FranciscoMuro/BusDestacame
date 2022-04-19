from django.db import models

# Create your models here.
class Pasajero(models.Model):
    pasajeroId = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre del pasajero", max_length=50)