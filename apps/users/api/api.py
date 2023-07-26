
from multiprocessing import context
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

@api_view(["GET","POST"])
def user_api_view(request):
    # list
    if request.method == "GET":
        # queryset
        users = User.objects.all()
        user_serializer = UserListSerializer(
            users,
            many = True
        )        
        return Response(
            user_serializer.data,
            status= status.HTTP_200_OK
        )
        
        
        
    # create
    elif request.method == 'POST':
        user_serializer = UserSerializer(
            data=request.data,
            context=request.data
        )
        # validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {
                    "message":"Usuario creado",
                    "data":user_serializer.data
                    },
                status= status.HTTP_201_CREATED
            )
        return Response(
            user_serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )



@api_view(["GET","PUT","DELETE"])
def user_detail_api_view(request,pk=None):
    #consulta / queryset
    user = User.objects.filter(id=pk).first()
    # validación / validation
    if user:
        # retrieve
        if request.method == "GET":
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializer(user)
            return Response(
                user_serializer.data,
                status= status.HTTP_200_OK
            )
        #update
        elif request.method == "PUT":
            # para actualizar, pasamos la instanca + la data
            user_serializer = UserSerializer( 
                user,
                data = request.data
            )
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(
                    user_serializer.data,
                    status= status.HTTP_200_OK
                )
            return Response(
                user_serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
            
        # delete
        elif request.method == "DELETE":
            user.delete()
            return Response(
                {"message":"Ususario eliminado correctamente"},
                status= status.HTTP_200_OK
            )
    
    return Response(
        {"message":"No se encontrado el usuario"},
        status= status.HTTP_404_NOT_FOUND
    )