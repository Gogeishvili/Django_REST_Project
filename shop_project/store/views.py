from django.http import JsonResponse
from . import models
from django.conf import settings
from django.forms.models import model_to_dict


def products_JSON_view(request):
    products = models.Product.objects.get_prodacts_JSON_data()
    return JsonResponse({"products": products})
