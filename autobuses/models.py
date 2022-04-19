from django.db import models
from choferes.models import Chofer
from trayectos.models import Trayecto

class Autobus(models.Model):
    busId = models.AutoField(primary_key=True)
    Chofer = models.ForeignKey(Chofer, verbose_name="Chofer del autobus", on_delete=models.CASCADE)
    trayecto = models.ForeignKey(Trayecto, verbose_name="Chofer del autobus", on_delete=models.CASCADE)