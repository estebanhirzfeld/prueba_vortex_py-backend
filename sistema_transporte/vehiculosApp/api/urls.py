from django.urls import path
from vehiculosApp.api.views import vehiculo_api_view, vehiculo_detail_view, vehiculos_asignados, vehiculos_no_asignados, asignar_conductor, quitar_asignacion

urlpatterns = [
    path('', vehiculo_api_view, name='vehiculos_api'),
    path("<int:pk>/", vehiculo_detail_view, name="vehiculo_detail_view"),
    path('asignados/<int:pk>/', vehiculos_asignados, name='vehiculos_asignados'),
    path('no-asignados/', vehiculos_no_asignados, name='vehiculos_no_asigandos'),
    path('asignar/', asignar_conductor, name='asignar'),
    path('quitar-asignacion/<int:pk>/', quitar_asignacion, name='quitar_asignacion'),
]