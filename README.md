# DJANGO REST FRAMEWORK

## Configuration
- Dentro del proyecto creamos una carpeta llamada ```settings.py```.
- Dentro de ````settings.py```` creamos tres archivos : ````base.py````, ````local.py```` y ````production.py````.
- Separamos las configuraciones base de las configuraciones de ````local```` y ````production````, las cuales son : **DEBUG**, **ALLOWED_HOSTS**, **DATABASES**,**STATIC_URL**.
- Luego entramos a ````wsgi.py```` y ````asgi.py```` y en la configuración colocamos en la que estemos trabajando ````os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.local.py')````

## APIs
### APIViews
```python
#api.py
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserAPIView(APIView):
    
    def get(self,request):
        users = User.objects.all()
        user_serializer = UserSerializer(
            users,
            many = True
        )
        return Response(
            data = user_serializer.data
        )
```
```python
#urls.py
from django.urls import path
from apps.users.api.api import UserAPIView

urlpatterns = [
    path('usuario/',UserAPIView.as_view(), name='usuario_api')
]

```


### @api_view
```python 
#api.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(["GET"])
def user_api_view(request):
    
    if request.method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(
            users,
            many = True
        )
        return Response(
            user_serializer.data
        )
```
```python
#urls.py
from django.urls import path
from apps.users.api.api import user_api_view

urlpatterns = [
    path('usuario/',user_api_view, name='usuario_api')
]

```

## Serializadores
Los serializadores nos permiten convertir un JSON en un objeto que pueda ser procesado por la base de datos y viceversa
```python 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude 
```

### Validaciones:
Los serializadores tienen diferentes validadores, algunos vienen por defecto cuando se enlazan con el modelo, pero estos validadores se pueden rescribir.
```python
# Definición del serializador
class TestUSerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_email(self,value):
        # Custom validation
        print(value)
        if value == "":
            # levantamiento de error en caso de validador
            raise serializers.ValidationError("email no puede ir vacio")
            # sí se cumple el validador, este error saldrá en la respuesta al JSON
        
        # podemos llamar otros validadores
        if self.validate_name(self.context["name"]) in value:
            raise serializers.ValidationError("El email no puede contener el nombre")
```