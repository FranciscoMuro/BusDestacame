from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#Serializer
from BusDestacame.serializers import PasajeroSerializer
#Models
from pasajeros.models import Pasajero


@csrf_exempt
def obtenerPasajeros(request):
    pasajeros = Pasajero.objects.all();
    pasajero_serializer=PasajeroSerializer(pasajeros, many=True)
    return JsonResponse(pasajero_serializer.data, safe=False);


@csrf_exempt
def crearNuevoPasajero(request):
    newPasajeroData = JSONParser().parse(request)
    pasajero_serializer=PasajeroSerializer(data=newPasajeroData)
    if pasajero_serializer.is_valid():
        pasajero_serializer.save()
        return JsonResponse("Nuevo Autobus fue creado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al agregar el nuevo autobus", safe=False)

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
    pasajero.delete()
    return JsonResponse("El pasajero eliminado exitosamente", safe=False)
