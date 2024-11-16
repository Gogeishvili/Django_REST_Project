from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "restaurant"


router = routers.DefaultRouter()
router.register(r"restaurants", views.RestaurantViewSet, basename="RestaurantViewSet")
router.register(r"ingredints", views.IngredientsViewSet, basename="IngredientsViewSet")
router.register(r"menus", views.MenuViewSet, basename="MenuViewSet")
router.register(r"categories", views.CategoryViewSet, basename="CategoryViewSet")
router.register(r"dishes", views.DishViewSet, basename="DishViewSet")

urlpatterns = [
    path("", include(router.urls)),
]