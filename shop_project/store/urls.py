from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("products/JSON", views.products_JSON_view, name="products_JSON_view"),
    path("category/JSON",views.category_JSON_view,name="category_JSON_view")
]
