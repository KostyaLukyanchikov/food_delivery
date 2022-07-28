import logging
from typing import List

from django.db import transaction
from django.db.models import Count, Sum, F
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from delivery.base_view import BaseView
from orders.models import OrderPosition, Order
from orders.serializers import OrdersSerializer
from shopping_cart.models import CartPosition


class OrdersApi(BaseView):

    @staticmethod
    def get(*args, **kwargs):
        result = OrderPosition.objects.aggregate(
            total_count=Count('order', distinct=True),
            total_sum=Sum(F('price') * F('quantity')),
        )
        orders = Order.objects.all().order_by(F('time').desc())[:10]
        result['last_orders'] = OrdersSerializer(orders, many=True).data
        return Response(result, status=200)

    @classmethod
    def post(cls, request: Request):
        with transaction.atomic():
            cart_positions = CartPosition.objects.all()
            if not cart_positions:
                raise ValidationError('cart is empty')

            order = Order()
            logging.info(f'created order {order}')

            order_positions, price = cls._create_positions(
                order=order,
                cart_positions=cart_positions
            )

            user = cls._get_validated_user(request=request, price=price)
            user.balance -= price
            user.save()

            order.price = price
            order.save()

            OrderPosition.objects.bulk_create(order_positions)

            cart_positions.delete()

        return Response(status=200)

    @staticmethod
    def _create_positions(order: Order, cart_positions: List[CartPosition]):
        price = 0
        order_positions = []
        for position in cart_positions:
            order_position = OrderPosition(
                dish_id=position.dish.id,
                name=position.dish.name,
                price=position.dish.price,
                quantity=position.quantity,
                order=order,
            )
            price += position.dish.price * position.quantity
            logging.info(f'created position: {order_position}')
            order_positions.append(order_position)
        return order_positions, price

    @staticmethod
    def _get_validated_user(request: Request, price: float):
        user = request.user
        if user.balance < price:
            msg = (
                f'not enough money! '
                f'balance: {user.balance}, total price: {price}'
            )
            logging.info(msg)
            raise ValidationError(msg)
        return user
