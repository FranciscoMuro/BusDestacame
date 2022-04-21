#Utils
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#Serializer
from BusDestacame.serializers import ChoferSerializer
#Models
from choferes.models import Chofer


@csrf_exempt
def obtenerChoferes(request):
    choferes = Chofer.objects.all();
    choferes_serializer=ChoferSerializer(choferes, many=True)
    return JsonResponse(choferes_serializer.data, safe=False);


@csrf_exempt
def crearNuevoChofer(request):
    newChoferData = JSONParser().parse(request)
    choferes_serializer=ChoferSerializer(data=newChoferData)
    if choferes_serializer.is_valid():
        choferes_serializer.save()
        return JsonResponse("Nuevo chofer agregado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al agregar el nuevo chofer", safe=False)

@csrf_exempt
def actualizarChofer(request, pk):
    newChoferData = JSONParser().parse(request)
    chofer = Chofer.objects.get(choferId = pk)
    choferes_serializer=ChoferSerializer(chofer, data=newChoferData)
    if choferes_serializer.is_valid():
        choferes_serializer.save()
        return JsonResponse("Chofer actualizado exitosamente", safe=False)
    return JsonResponse("Algo salio mal al actualizar la informacion del chofer", safe=False)

@csrf_exempt
def eliminarChofer(request, pk):
    chofer = Chofer.objects.get(choferId = pk)
    chofer.delete()
    return JsonResponse("Chofer "+chofer.nombre+" eliminado exitosamente", safe=False)