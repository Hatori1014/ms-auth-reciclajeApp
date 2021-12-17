from rest_framework import serializers
from reciclajeAplicacion.models.autenticacion import Autenticacion

class AutenticacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autenticacion
        fields = ['id', 'username', 'password', 'name', 'email', 'phone', 'address']