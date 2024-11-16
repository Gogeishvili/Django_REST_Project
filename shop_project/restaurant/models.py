from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    cover_image = models.ImageField(upload_to="restaurant_covers/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")

    def __str__(self):
        return self.name


# class MenuCategory(models.Model):
#     name = models.CharField(max_length=100)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_categories')

#     def __str__(self):
#         return self.name

# class SubMenuCategory(models.Model):
#     name = models.CharField(max_length=100)
#     cover_image = models.ImageField(upload_to='submenu_covers/', null=True, blank=True)
#     parent_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='sub_categories')

#     def __str__(self):
#         return self.name

# class Dish(models.Model):
#     name = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='dish_photos/', null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     sub_category = models.ForeignKey(SubMenuCategory, on_delete=models.CASCADE, related_name='dishes')
#     ingredients = models.ManyToManyField('Ingredient', related_name='dishes')

#     def __str__(self):
#         return self.name

# class Ingredient(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
