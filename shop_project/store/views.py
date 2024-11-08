from django.http import JsonResponse
from store import models
from django.conf import settings

# Create your views here.
def index(request):
    products = list(models.Product.objects.values())

    # Add the full image URL by combining the media URL with the relative image path
    for product in products:
        if product.get('image'):
            product['image_url'] = settings.MEDIA_URL + product['image']

    return JsonResponse({"products": products})