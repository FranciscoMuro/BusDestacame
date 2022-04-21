from django.urls import path
from .views import (obtenerPasajeros, crearNuevoPasajero, actualizarPasajero, eliminarPasajero)

app_name = 'pasajeros'

urlpatterns = [
    path('obtener/', obtenerPasajeros, name='obtenerpasajeros'),
    path('crear/', crearNuevoPasajero, name='crearpasajero'),
    path('actualizar/<int:pk>', actualizarPasajero, name='actualizarpasajero'),
    path('eliminar/<int:pk>', eliminarPasajero, name='eliminarpasajero'),
]
