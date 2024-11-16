from django.http import JsonResponse
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from . import serializers
from rest_framework import status
from rest_framework import views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication


def products_JSON_view(request):
    products = models.Product.objects.get_prodacts_data_list()
    return JsonResponse({"products": products})


def categories_JSON_view(request):
    categories = models.Category.objects.get_categories_data_list()
    return JsonResponse({"categopries": categories})


def tags_JSON_view(request):
    tags = models.Tag.objects.get_tags_data_list()
    return JsonResponse({"tags": tags})


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def products_API_view(request):
    product_data = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer = serializers.ProductSerializer(
        product_data, many=True, context={"request": request}
    )
    return Response(serializer.data)


class ProductsViewAPI(views.APIView):
    def get(self, request):
        product_data = models.Product.objects.all().prefetch_related(
            "categories", "tags"
        )
        serializer = serializers.ProductSerializer(
            product_data, many=True, context={"request": request}
        )
        return Response(serializer.data)


class ProductDetailViewAPI(generics.RetrieveAPIView):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductListViewAPI(generics.ListAPIView):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class=PageNumberPagination


class CreateProductView(generics.CreateAPIView):
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]


class ListCreateProductView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]


class UpdateProductView(generics.UpdateAPIView):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all().prefetch_related("categories", "tags")
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication,authentication.SessionAuthentication,JWTAuthentication]

    @action(detail=True, methods=["POST"])
    def set_zero(self, request, **kwargs):
        product = self.get_object()
        product.quantity = 0
        product.save()
        serializer = self.get_serializer()
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["GET"],
        serializer_class=serializers.ProductModelSerializer,
    )
    def only_zero(self, request, **kwargs):
        products = models.Product.objects.filter(quantity=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
