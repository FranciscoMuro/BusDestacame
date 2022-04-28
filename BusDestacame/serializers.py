from rest_framework import serializers
from autobuses.models import Autobus
from choferes.models import Chofer
from pasajeros.models import Pasajero
from trayectos.models import Trayecto

class AtobusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autobus
        fields=('busId', 'chofer', 'trayecto', 'fecha_salida', 'hora_salida', 'procentajeDePasajeros')

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chofer
        fields=('choferId', 'nombre')

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pasajero
        fields=('pasajeroId', 'nombre', 'autobus')

class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trayecto
        fields=('trayectoId', 'origen', 'destino')