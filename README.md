# DJANGO REST FRAMEWORK

## Credenciales
- Usuario 1:
  - felipegonzalezq
  - luna1503
- Usuario 2:
  - felipe2
  - luna1503



## Ambiente virutal y Settings
```powershell
# creamos entorno virtual
python -m virtualenv venv

# activamos el entorno virtual
.\venv\Scripts\activate

# instalamos django en el entorno
pip install django

# creamos el project
django-admin startproject [projecto] .
```

## Primeros pasos
```powershell
# Registramos los cambios para las migraciones
python manage.py makemigrations

# realizamos las migraciones predeterminadas sqlite
python manage.py migrate

# Corremos el servidor
python manage.py runserver
```


## Creamos una app.
- A la altura de ```manage.py``` escribimos el comando ```python manage.py startapp [App]```.
- Luego nos dirigimos a ```settings.py``` en INSTALLED_APPS agregamos nuestra app.
- ![](./imagenes/app.jpg)
- ![](./imagenes/app_in_settings.jpg)

## Creación de un modelo.
- Entramos al archivo ```models.py``` dentro de nuestra aplicación.
- Creamos nuestros modelos extendiendo la clase ```models``` de ```django.db```.
- ![](./imagenes/modelos.jpg)
- Para hacer las migraciones debemos escribir el comando ```python manage.py makemigrations```.
- Para aplicar las migraciones ```python manage.py migrate```.



## Configuration
### django-jazzmin
- Install the latest pypi release with ````pip install -U django-jazzmin````
- Add ````jazzmin```` to your ````INSTALLED_APPS```` before ````django.contrib.admin````.
```python
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    [...]
]
```
### Django-jazzmin full example
To configure the general behaviour of ````jazzmin````, you can use ````JAZZMIN_SETTINGS```` within your django ````settings````, below is a full example, with some of the more complex items explained below that.
```python
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Library Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Library",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Library",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the library",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": True,
}
```` 


### Project Settings
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