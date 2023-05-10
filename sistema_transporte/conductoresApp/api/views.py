import sistema_transporte.helpers as res
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from conductoresApp.api.serializers import ConductorSerializer
from conductoresApp.models import Conductor
from rest_framework import status
from rest_framework.response import Response
from vehiculosApp.api.serializers import VehiculoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from vehiculosApp.models import Vehiculo


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def conductor_api_view(request):

    # List users
    if request.method == 'GET':
        conductores = Conductor.objects.all().values('id', 'nombre', 'apellido', 'telefono', 'identificacion', 'direccion')
        conductores_serializer = ConductorSerializer(conductores, many=True)
        return Response({'message': 'Lista de conductores', 'data': conductores_serializer.data}, status=status.HTTP_200_OK)
    
    # Create user
    elif request.method == 'POST':
        conductores_serializer = ConductorSerializer(data=request.data)
        if conductores_serializer.is_valid():
            conductores_serializer.save()
            return Response({'message': 'Creación exitosa', 'data': conductores_serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Algo salió mal', 'errors': conductores_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def conductor_detail_view(request, pk):
    #Queryset (Consultar si el conductor existe)
    conductor = Conductor.objects.filter(id=pk).first()
    if conductor:
        # Find conductor by id
        if request.method == 'GET':
            conductor_serializer = ConductorSerializer(conductor)
            return Response({'message': 'Búsqueda exitosa', 'data': conductor_serializer.data}, status=status.HTTP_200_OK)
        
        # Update conductor
        elif request.method == 'PUT':
            conductor_serializer = ConductorSerializer(conductor, data=request.data)
            if conductor_serializer.is_valid():
                conductor_serializer.save()
                return Response({'message': 'Actualización exitosa', 'data': conductor_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message': 'Algo salió mal', 'errors': conductor_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        # Delete conductor
        elif request.method == 'DELETE':
            conductor.delete()
            return Response({'message': 'Conductor eliminado'}, status=status.HTTP_200_OK)
        
    return Response({'message': 'El conductor no fue encontrado'}, status=status.HTTP_400_BAD_REQUEST)
