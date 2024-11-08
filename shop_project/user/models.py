from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["email"]

    objects=CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff or self.is_superuser
