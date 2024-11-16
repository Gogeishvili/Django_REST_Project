from rest_framework import viewsets, permissions, status
from rest_framework.serializers import *
from rest_framework.response import Response
from . import serializers as s
from . import models as m


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = m.Restaurant.objects.all()
    serializer_class = s.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return []
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.serializer_class = s.RestaurantViewSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = s.RestaurantViewSerializer
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise ValidationError("You are not the owner")

        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = m.Ingredient.objects.all()
    serializer_class = s.IngredinetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise ValidationError("You are not the owner")

        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = m.Menu.objects.all()
    serializer_class = s.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise ValidationError("You are not the owner")

        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise ValidationError("You are not the owner")

        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)

class DishViewSet(viewsets.ModelViewSet):
    queryset = m.Dish.objects.all()
    serializer_class = s.DishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        if restaurant.owner != request.user:
            raise ValidationError("You are not the owner")

        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)
