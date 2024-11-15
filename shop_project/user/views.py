from django.http import JsonResponse
from . import models
from rest_framework import generics
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from . import parmitions





class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [parmitions.IsOwnerOrReadOnly] 

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateUserSerializer
        return serializers.UserSerializer
