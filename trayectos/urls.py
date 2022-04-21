from django.urls import path
from .views import (obtenerTrayectos, crearNuevoTrayecto, actualizarTrayecto, eliminarTrayecto)

app_name = 'trayectos'

urlpatterns = [
    path('obtener/', obtenerTrayectos, name='obtenertrayectos'),
    path('crear/', crearNuevoTrayecto, name='creartrayecto'),
    path('actualizar/<int:pk>', actualizarTrayecto, name='actualizartrayecto'),
    path('eliminar/<int:pk>', eliminarTrayecto, name='eliminartrayecto'),
]
