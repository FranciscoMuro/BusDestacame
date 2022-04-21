import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#Serializer
from BusDestacame.serializers import TrayectoSerializer
#Models
from trayectos.models import Trayecto


@csrf_exempt
def obtenerTrayectos(request):
    trayectos = Trayecto.objects.all();
    trayecto_serializer=TrayectoSerializer(trayectos, many=True)
    return JsonResponse(trayecto_serializer.data, safe=False);


@csrf_exempt
def crearNuevoTrayecto(request):
    newTrayectoData = JSONParser().parse(request)
    trayecto_serializer=TrayectoSerializer(data=newTrayectoData)
    if trayecto_serializer.is_valid():
        trayecto_serializer.save()
        return JsonResponse("Nuevo trayecto fue agregado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al agregar el nuevo trayecto", safe=False)

@csrf_exempt
def actualizarTrayecto(request, pk):
    newTrayectoData = JSONParser().parse(request)
    trayecto = Trayecto.objects.get(trayectoId = pk)
    trayecto_serializer=TrayectoSerializer(trayecto, data=newTrayectoData)
    if trayecto_serializer.is_valid():
        trayecto_serializer.save()
        return JsonResponse("El trayecto fue actualizado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al actualizar la informacion del trayecto", safe=False)

@csrf_exempt
def eliminarTrayecto(request, pk):
    trayecto = Trayecto.objects.get(trayectoId = pk)
    trayecto.delete()
    return JsonResponse("Trayecto "+trayecto.origen+"-"+trayecto.destino
    +" eliminado exitosamente", safe=False)