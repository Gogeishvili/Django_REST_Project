from rest_framework import serializers
from . import models


class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()
    image = serializers.ImageField()
    sum_price = serializers.SerializerMethodField(
        method_name="get_sum_price"
    ) 
    categories = serializers.SerializerMethodField(
        method_name="get_categories"
    )  
    tags=serializers.SerializerMethodField(method_name="get_tags")

    def get_categories(self, obj):
        return [
            {"id": category.id, "name": category.name}
            for category in obj.categories.all()
        ]

    def get_tags(self, obj):
        return [
            {"id": tag.id, "name": tag.name}
            for tag in obj.tags.all()
        ]

    def get_sum_price(self, object):
        return object.sum_price()


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"


class TagModelSerializer(serializers.Serializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
    categories = CategoryModelSerializer(many=True)
    tags = TagModelSerializer(many=True)

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


