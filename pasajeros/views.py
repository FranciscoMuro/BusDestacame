import imp
from operator import truediv
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#Serializer
from BusDestacame.serializers import PasajeroSerializer
from BusDestacame.serializers import AtobusSerializer
#Models
from pasajeros.models import Pasajero
from autobuses.models import Autobus


@csrf_exempt
def obtenerPasajeros(request):
    pasajeros = Pasajero.objects.all()
    pasajero_serializer=PasajeroSerializer(pasajeros, many=True)
    return JsonResponse(pasajero_serializer.data, safe=False)


@csrf_exempt
def crearNuevoPasajero(request):
    newPasajeroData = JSONParser().parse(request)
    actualizarPorcentajePasajeros(newPasajeroData['autobus'], True)
    pasajero_serializer=PasajeroSerializer(data=newPasajeroData)
    if pasajero_serializer.is_valid():
        pasajero_serializer.save()
        return JsonResponse("Nuevo Pasajer fue creado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al agregar el nuevo pasajero", safe=False)

@csrf_exempt
def actualizarPasajero(request, pk):
    newPasajeroData = JSONParser().parse(request)
    pasajero = Pasajero.objects.get(pasajeroId = pk)
    pasajero_serializer=PasajeroSerializer(pasajero, data=newPasajeroData)
    if pasajero_serializer.is_valid():
        pasajero_serializer.save()
        return JsonResponse("El pasajero fue actualizado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al actualizar la informacion del pasajero", safe=False)

@csrf_exempt
def eliminarPasajero(request, pk):
    pasajero = Pasajero.objects.get(pasajeroId = pk)
    actualizarPorcentajePasajeros(pasajero.autobus.busId, False)
    pasajero.delete()
    return JsonResponse("El pasajero eliminado exitosamente", safe=False)

def actualizarPorcentajePasajeros(pk, agregar):
    autobus = Autobus.objects.get(busId = pk)
    if (agregar):
        autobus.procentajeDePasajeros += 10
    else:
        autobus.procentajeDePasajeros -= 10
    autobus.save()
