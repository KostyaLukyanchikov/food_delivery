import logging

import rest_framework.exceptions
from rest_framework.exceptions import ParseError
from rest_framework.request import Request
from rest_framework.response import Response

from delivery.base_view import BaseView
from shopping_cart import models, serializers


class CartApi(BaseView):

    @staticmethod
    def get(*args, **kwargs):
        data = models.CartPosition.objects.all()
        serializer = serializers.CartGetSerializer(data, many=True)
        positions = list(serializer.data)
        total = sum(p['price'] for p in positions)
        result = {'total_price': total, 'positions': positions}
        return Response(result)

    @classmethod
    def post(cls, request: Request):
        data = cls._validated_data(request)
        serializer = serializers.CartCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            msg = f'dish with id {data["dish"]} does not exist'
            raise rest_framework.exceptions.NotFound(msg)

        return Response(status=200)

    @classmethod
    def delete(cls, request: Request):
        data = cls._validated_data(request)
        models.CartPosition.delete_position(
            dish=data['dish'],
            quantity=data['quantity']
        )
        return Response(status=200)

    @staticmethod
    def _validated_data(request: Request):
        try:
            dish = request.data['dish_id']
            quantity = request.data['quantity']
            result = {'dish': int(dish), 'quantity': int(quantity)}
            logging.info(f'data: {result}')
            return result
        except (KeyError, ValueError):
            raise ParseError('dish_id <int> and quantity <int> are required')
