from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from vehiculosApp.api.serializers import VehiculoSerializer
from vehiculosApp.models import Vehiculo
from rest_framework import status
from rest_framework.response import Response
import sistema_transporte.helpers as res
# import isAdmin
from rest_framework.permissions import IsAdminUser, IsAuthenticated




@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def vehiculo_api_view(request):
    
    #List
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        vehiculos_serializer = VehiculoSerializer(vehiculos, many=True)
        return Response({'message': 'Lista de vehiculos', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
    
    #Create user
    elif request.method == 'POST':
        vehiculos_serializer = VehiculoSerializer(data=request.data)
        if vehiculos_serializer.is_valid():
            vehiculos_serializer.save()
            return Response({'message': 'Creación exitosa', 'data': vehiculos_serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vehiculo_detail_view(request, pk):

    #Queryset (Consultar si el vehiculo existe)
    vehiculo = Vehiculo.objects.filter(id=pk).first()
    if vehiculo:
            
            #Find vehiculo by id
            if request.method == 'GET':
                vehiculos_serializer = VehiculoSerializer(vehiculo)
                return Response({'message': 'Búsqueda exitosa', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
            
            
            #Update user
            elif request.method == 'PUT':
                request.data
                vehiculos_serializer = VehiculoSerializer(vehiculo, data=request.data)
                if vehiculos_serializer.is_valid():
                    vehiculos_serializer.save()
                    return Response({'message': 'Actualización exitosa', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
    
                return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
            #Delete user
            elif request.method == 'DELETE':
                vehiculo.delete()
                return Response({'message': 'Eliminación exitosa', 'data': {}}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
def vehiculos_asignados(request, pk):

    # Queryset (Consultar si el vehiculo existe)
    vehiculos = Vehiculo.objects.filter(conductor_id=pk)
    if vehiculos:

        # Find vehiculo by conductor id
        if request.method == 'GET':
            vehiculos_serializer = VehiculoSerializer(vehiculos, many=True)
            return Response({'message': 'Vehículos asociados', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
        
        # Update vehiculo
        elif request.method == 'PUT':
            request.data
            vehiculo = Vehiculo.objects.filter(id=request.data.get('id')).first()
            vehiculos_serializer = VehiculoSerializer(vehiculo, data=request.data)
            if vehiculos_serializer.is_valid():
                vehiculos_serializer.save()
                return Response({'message': 'Actualización exitosa', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vehiculos_no_asignados(request):
        
        vehiculos = Vehiculo.objects.filter(conductor_id=None)
        if vehiculos:
    
            # Find vehiculo by conductor id
            if request.method == 'GET':
                vehiculos_serializer = VehiculoSerializer(vehiculos, many=True)
                return Response({'message': 'Vehículos no asociados', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
            
            # Update vehiculo
            elif request.method == 'PUT':
                request.data
                vehiculo = Vehiculo.objects.filter(id=request.data.get('id')).first()
                vehiculos_serializer = VehiculoSerializer(vehiculo, data=request.data)
                if vehiculos_serializer.is_valid():
                    vehiculos_serializer.save()
                    return Response({'message': 'Actualización exitosa', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
                return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'No se han encontrado vehículos con estos datos', 'data': {}}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def asignar_conductor(request):
    print('este es el id', request.data.get('id'))
    vehiculo = Vehiculo.objects.filter(id=request.data.get('id')).first()

    if vehiculo:

        if request.method == 'PUT':
                
                vehiculos_serializer = VehiculoSerializer(vehiculo, data=request.data)
                if vehiculos_serializer.is_valid() and vehiculo.conductor_id == None:
                    vehiculos_serializer.save()
                    return Response({'message': 'Asignación completa', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
                return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'No se han encontrado vehículos con estos datos', 'data': {}}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def quitar_asignacion(request, pk):
        vehiculo = Vehiculo.objects.filter(id=request.data.get('id')).first()
    
        if vehiculo:
    
            if request.method == 'PUT':
                    request.data
                    vehiculos_serializer = VehiculoSerializer(vehiculo, data=request.data)
                    if vehiculos_serializer.is_valid():
                        vehiculos_serializer.save()
                        return Response({'message': 'Se quita asignación', 'data': vehiculos_serializer.data}, status=status.HTTP_200_OK)
                    return Response({'message': 'Algo salió mal', 'errors': vehiculos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'No se han encontrado vehículos con estos datos', 'data': {}}, status=status.HTTP_400_BAD_REQUEST)