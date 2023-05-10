from rest_framework.views import APIView
from rest_framework.decorators import api_view
from conductoresApp.api.serializers import ConductorSerializer
from pedidosApp.models import Conductor
from rest_framework import status
from rest_framework.response import Response
from pedidosApp.api.serializers import PedidoSerializer

from pedidosApp.models import Pedido

@api_view(['GET', 'POST'])
def pedido_api_view(request):
    
        #List users
        if request.method == 'GET':        
            pedidos = Pedido.objects.all().values('id', 'fecha', 'hora', 'direccion', 'descripcion', 'estado', 'conductor')
            pedidos_serializer  = PedidoSerializer(pedidos, many = True)
            return  Response(pedidos_serializer.data, status= status.HTTP_200_OK)
        
        #Create user
        elif request.method == 'POST':
            pedidos_serializer = PedidoSerializer(data = request.data)
            if pedidos_serializer.is_valid():
                pedidos_serializer.save()
                return Response(pedidos_serializer.data,status= status.HTTP_201_CREATED)
            
            return Response({'message': 'Algo salió mal', 'errors': pedidos_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def pedido_detail_view(request, pk):

    #Queryset (Consultar si el usuario existe)
    pedido = Pedido.objects.filter(id=pk).first()
    if pedido:

        #Find pedido by id
        if request.method == 'GET':
            pedidos_serializer = PedidoSerializer(pedido)
            return Response(pedidos_serializer.data, status=status.HTTP_200_OK)
        
        #Update pedido
        elif request.method == 'PUT':
            request.data
            pedidos_serializer = PedidoSerializer(pedido, data = request.data)
            if pedidos_serializer.is_valid():
                pedidos_serializer.save()
                return Response(pedidos_serializer.data , status= status.HTTP_200_OK)
            return Response(pedidos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #Delete pedido
        elif request.method == 'DELETE':
            pedido.delete()
            return Response({'message': 'Pedido eliminado correctamente!'} , status= status.HTTP_200_OK)
    return Response({'message': 'El pedido no fue encontrado' }, status = status.HTTP_400_BAD_REQUEST)
