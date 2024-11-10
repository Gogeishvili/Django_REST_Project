from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("products/JSON", views.products_JSON_view, name="products_JSON_view"),
    path("categories/JSON",views.categories_JSON_view,name="categories_JSON_view"),
    path("tags/JSON",views.tags_JSON_view,name="tags_JSON_view"),
    path("products/API",views.products,name="products")
]
