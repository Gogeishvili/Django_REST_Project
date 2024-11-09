from django.http import JsonResponse
from . import models


def index(request):
    users_list = list(models.CustomUser.objects.values())
    return JsonResponse({"users": users_list})
