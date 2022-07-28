from rest_framework import serializers

from menu import models as menu_models
from menu import serializers as menu_serializers
from . import models


class CartCreateSerializer(serializers.ModelSerializer):
    dish = serializers.PrimaryKeyRelatedField(
        queryset=menu_models.Dish.objects.all()
    )

    class Meta:
        model = models.CartPosition
        fields = ['dish', 'quantity']


class CartGetSerializer(serializers.ModelSerializer):
    dish = menu_serializers.DishSerializer()

    class Meta:
        model = models.CartPosition
        fields = ['dish', 'quantity']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(data.pop('dish'))
        data['price'] *= data['quantity']
        return data
