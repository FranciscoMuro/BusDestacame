from django.urls import path
from .views import (obtenerChoferes, crearNuevoChofer, actualizarChofer, eliminarChofer)

app_name = 'choferes'

urlpatterns = [
    path('obtener/', obtenerChoferes, name='obtenerchofer'),
    path('crear/', crearNuevoChofer, name='crearchofer'),
    path('actualizar/<int:pk>', actualizarChofer, name='actualizarchofer'),
    path('eliminar/<int:pk>', eliminarChofer, name='eliminarchofer'),
]
