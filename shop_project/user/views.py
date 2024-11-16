from django.http import JsonResponse
from . import models
from rest_framework import generics
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from . import parmitions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserPageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication,authentication.SessionAuthentication,JWTAuthentication]

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.CreateUserSerializer
        return serializers.UserPageSerializer
