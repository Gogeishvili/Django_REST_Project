from django.http import JsonResponse
from store import models

# Create your views here.
def index(request):
    products=list(models.Product.objects.values())
    return JsonResponse({"products":products})