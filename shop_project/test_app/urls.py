from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "test_app"

router = routers.DefaultRouter()
router.register(r"tests", views.ProductViewSet, basename="ProductViewSet")


urlpatterns = [
    path("products/JSON", views.products_JSON_view, name="products_JSON_view"),
    path("categories/JSON", views.categories_JSON_view, name="categories_JSON_view"),
    path("tags/JSON", views.tags_JSON_view, name="tags_JSON_view"),
    path("products/API", views.products_API_view, name="products_API_view"),
    path("ProductsViewAPI/", views.ProductsViewAPI.as_view(), name="ProductsViewAPI"),
    path(
        "ProductDetailViewAPI/<int:pk>/",
        views.ProductDetailViewAPI.as_view(),
        name="ProductDetailViewAPI",
    ),
    path(
        "ProductListViewAPI/",
        views.ProductListViewAPI.as_view(),
        name="ProductListViewAPI",
    ),
    path(
        "CreateProductView/",
        views.CreateProductView.as_view(),
        name="CreateProductView",
    ),
    path(
        "ListCreateProductView/",
        views.ListCreateProductView.as_view(),
        name="ListCreateProductView",
    ),
    path(
        "UpdateProductView/<int:pk>",
        views.UpdateProductView.as_view(),
        name="UpdateProductView",
    ),
    path(
        "RetrieveUpdateDestroyProductView/<int:pk>",
        views.RetrieveUpdateDestroyProductView.as_view(),
        name="UpdateProductView",
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
   
]
