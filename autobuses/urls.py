from django.urls import path
from .views import (obtenerAutobuses, crearNuevoAutobus, actualizarAutobus, eliminarAutobus)

app_name = 'autobuses'

urlpatterns = [
    path('obtener/', obtenerAutobuses, name='obtenerautobuses'),
    path('crear/', crearNuevoAutobus, name='crearautobus'),
    path('actualizar/<int:pk>', actualizarAutobus, name='actualizarautobus'),
    path('eliminar/<int:pk>', eliminarAutobus, name='eliminarautobus'),
]
