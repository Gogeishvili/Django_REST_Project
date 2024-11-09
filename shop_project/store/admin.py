from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "is_active", "sum_price"] 
    list_editable = ["price", "quantity", "is_active"]  
    list_display_links = ["name"] 
    prepopulated_fields = {"slug": ("name",)}


    @admin.display(description="Sum Price")
    def sum_price(self, obj):
        return obj.sum_price()
    

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    list_display_links=['name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']


