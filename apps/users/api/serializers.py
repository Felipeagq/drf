from rest_framework import serializers
from apps.users.models import User

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
        if self.validate_name(self.context["name"]) in value:
            raise serializers.ValidationError("El email no puede contener el nombre")
            
        return value
    
    def validate(self,data):
        # Esto lanza un error sin campo
        # if data["name"] in data["email"]:
        #     raise serializers.ValidationError("El email no puede contener el nombre")
        print(data)
        return data