from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users  # Utiliza la clase del modelo Users
        fields = '__all__'
        read_only_fields = ('created_at', )
