# DJANGO REST FRAMEWORK

## Credenciales
- Usuario 1:
  - felipegonzalezq
  - luna1503
- Usuario 2:
  - felipe2
  - luna1503

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


class TestUSerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    
    def validate_name(self,value):
        # Custom validation
        print(value)
        print(self.context)
        if "test" in value:
            raise serializers.ValidationError("error, no puede existir un usuario con ese nombre")
        return value
    
    def validate_email(self,value):
        # Custom validation
        print(value)
        
        if value == "":
            raise serializers.ValidationError("email no puede ir vacio")
        
        # podemos llamar otros validadores
        # if self.validate_name(self.context["name"]) in value:
        #     raise serializers.ValidationError("El email no puede contener el nombre")
            
        return value
    
    def validate(self,data):
        # Esto lanza un error sin campo
        # if data["name"] in data["email"]:
        #     raise serializers.ValidationError("El email no puede contener el nombre")
        print(data)
        return data
    
    # def create(self,validate_data):
    #     return self.model.object.create(**validate_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name",instance.name)
    #     instance.email = validated_data.get("email",instance.email)
    #     instance.save()
    #     return instance
    
    def save(self):
        print(f"impresión de instancia: {self}")

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

    # Función que valida la data en general
    def validate(self,data):
        ...
        return validate_data
```

### Metodo Create:
Cuando uno esta trabajando con serializadores, despues de usar el metodo validate, uno usa el metodo create, el cual guarda en base de datos, pero esta función internamente llama al ORM de Django.
```python
# Definición del serializador
class TestUSerSerializer(serializers.Serializer):
    ...
    # Función que valida la data en general
    def validate(self,data):
        ...
        return validate_data

    # "self.model" debe ser un modelo creado
    def create(self,validate_data):
        return self.model.objects.create(**validate_data)
```


### Metodo Update:
```python
# Definición del serializador
class TestUSerSerializer(serializers.Serializer):
    ...
    # Función que valida la data en general
    def validate(self,data):
        ...
        return validate_data

    # "self.model" debe ser un modelo creado
    def create(self,validate_data):
        ...
    
    # llamado cuando se define un objeto de serializador
    # con (instance= , data= )
    def update(self,instance, validate_data):
        # recorre la instancia asignandole el nuevo valor 
        # de validate_data
        # Esto por cada atributo de la instancia, definido en los fields
        instance.field = validate_data.get("field",instance.field)
        instance.save()
        return instance
```

### Metodo save:
```python
# Definición del serializador
class TestUSerSerializer(serializers.Serializer):
    ...

    def validate(self,data):
        ...
        return validate_data

    def create(self,validate_data):
        ...
    
    def update(self,instance, validate_data):
        ...
    
    # aqui se pueden hacer operaciones que se tengan que ejecutar cuando
    # se registra un dato en la base de datos,
    # un envio de notificación, envio de correo, confirmación.
    # También puedo redistribuirlo en otro modelo.
    def save(self):
        # podemos acceder a "validated_data"
        # ya que hace parte del mismo obejto
        print(self.validated_data)
```


### Anotaciones:
```python
@api_view(["POST","GET","PU"])
def testing_api_view(request,pk=None):
    if request.method == "GET":
        # solo se para el objeto
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
    
    elif request.method == "POST":
        # se usa el "data ="
        user_serializer = UserSerializer(data=request.data)

    elif request.method == "PUT":
        # Se pasa el modelo y el data
        user_serializer = UserSerializer(user, data=request.data)

```