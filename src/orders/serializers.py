from rest_framework import serializers

from . import models


class OrderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderPosition
        fields = ['dish_id', 'name', 'price', 'quantity']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] *= data['quantity']
        data['id'] = data.pop('dish_id')
        return data


class OrdersSerializer(serializers.ModelSerializer):
    positions = OrderPositionSerializer(many=True)

    class Meta:
        model = models.Order
        fields = ['id', 'price', 'time', 'positions']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['time'] = int(instance.time.timestamp())
        return data
