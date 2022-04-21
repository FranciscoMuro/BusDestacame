#Utils
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#Serializer
from BusDestacame.serializers import AtobusSerializer
#Models
from autobuses.models import Autobus

@csrf_exempt
def obtenerAutobuses(request):
    autobuses = Autobus.objects.all();
    autobus_serializer=AtobusSerializer(autobuses, many=True)
    return JsonResponse(autobus_serializer.data, safe=False);


@csrf_exempt
def crearNuevoAutobus(request):
    newAutobusData = JSONParser().parse(request)
    autobus_serializer=AtobusSerializer(data=newAutobusData)
    if autobus_serializer.is_valid():
        autobus_serializer.save()
        return JsonResponse("Nuevo Autobus fue creado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al agregar el nuevo autobus", safe=False)

@csrf_exempt
def actualizarAutobus(request, pk):
    newAutobusData = JSONParser().parse(request)
    autobus = Autobus.objects.get(busId = pk)
    autobus_serializer=AtobusSerializer(autobus, data=newAutobusData)
    if autobus_serializer.is_valid():
        autobus_serializer.save()
        return JsonResponse("El autobus fue actualizado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al actualizar la informacion del autobus", safe=False)

@csrf_exempt
def eliminarAutobus(request, pk):
    autobus = Autobus.objects.get(busId = pk)
    autobus.delete()
    return JsonResponse("El autobus eliminado exitosamente", safe=False)