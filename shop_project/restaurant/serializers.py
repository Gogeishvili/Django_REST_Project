from rest_framework import serializers
from . import models as m


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Restaurant
        fields = "__all__"

class RestaurantViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Restaurant
        fields = ["id", "name"]


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Restaurant
        fields = "__all__"

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
    


class IngredinetSerializer(serializers.ModelSerializer):
    class Meta:
        model=m.Ingredient
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=m.Category
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)




class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=m.Menu
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
    

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model=m.Dish
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
