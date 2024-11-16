from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "restaurant"


router = routers.DefaultRouter()
router.register(r"restaurants", views.RestaurantViewSet, basename="RestaurantViewSet")

urlpatterns = [
    path("", include(router.urls)),
]