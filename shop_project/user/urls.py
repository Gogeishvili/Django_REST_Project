from django.urls import path,include
from . import views
from rest_framework import routers

app_name = "user"


router=routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
