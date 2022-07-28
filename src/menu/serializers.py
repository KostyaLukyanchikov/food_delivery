from rest_framework import serializers

from . import models


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'price']


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = models.Restaurant
        fields = ['id', 'name', 'dishes']
