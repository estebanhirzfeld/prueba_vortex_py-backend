
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework import status

from .models import User

from .serializer import UserSerializer, UserListSerializer

from backend_prueba.helpers import response
# Create your views here.

# @csrf_exempt
class UserCreateView(CreateAPIView):
    
    
    # @csrf_exempt
    def post(self, request):

        try:
            data = request.data
            serializer_class = UserSerializer(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(response.success(serializer_class.data, status.HTTP_201_CREATED, 'Usuario creado'), status.HTTP_201_CREATED )
            else:
                return Response(response.serverError(serializer_class.errors, status.HTTP_409_CONFLICT, 'Faltan datos'), status.HTTP_409_CONFLICT )

        except Exception as err :
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal' ), status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class UserListView(ListCreateAPIView):
    queryset = User.objects.all().values('id', 'name', 'lastname', 'email')
    serializer_class = UserListSerializer
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        try:

            queryset = self.get_queryset()
            serializer = UserListSerializer(queryset, many=True)
            return Response(response.success(serializer.data, 200, 'Lista de usuarios'))
        except Exception as err:
            return Response(response.serverError(err, 500, 'Algo salio mal'))