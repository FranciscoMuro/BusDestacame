from django.db import models

# Create your models here.

class Chofer(models.Model):
    choferId = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre del cofer", max_length=50);

    def __str__(self):
        return self.nombre