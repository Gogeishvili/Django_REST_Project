from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("products/JSON", views.products_JSON_view, name="products_JSON_view"),
]
