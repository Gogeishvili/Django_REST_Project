from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CustomUser
        fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CustomUser
        fields=['name','email','password']
    
    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user