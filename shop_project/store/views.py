from django.http import JsonResponse
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound


def products_JSON_view(request):
    products = models.Product.objects.get_prodacts_data_list()
    return JsonResponse({"products": products})


def categories_JSON_view(request):
    categories = models.Category.objects.get_categories_data_list()
    return JsonResponse({"categopries": categories})


def tags_JSON_view(request):
    tags = models.Tag.objects.get_tags_data_list()
    return JsonResponse({"tags": tags})

@api_view()
def products(request):
    products=models.Product.objects.values()
    products = models.Product.objects.get_prodacts_data_list()
    return Response(list(products))
