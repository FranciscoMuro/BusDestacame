from rest_framework import serializers
from autobuses.models import Autobus
from choferes.models import Chofer
from pasajeros.models import Pasajero
from trayectos.models import Trayecto

class AtobusSerializer(serializers.modelSerializer):
    class Meta:
        model=Autobus
        fields=('busId', 'Chofer', 'trayecto')

class ChoferSerializer(serializers.modelSerializer):
    class Meta:
        model=Chofer
        fields=('choferId', 'nombre')

class PasajeroSerializer(serializers.modelSerializer):
    class Meta:
        model=Pasajero
        fields=('pasajeroId', 'nombre')

class TrayectoSerializer(serializers.modelSerializer):
    class Meta:
        model=Trayecto
        fields=('trayectoId', 'choferId', 'origen', 'destino', 'fecha_hora_salida')