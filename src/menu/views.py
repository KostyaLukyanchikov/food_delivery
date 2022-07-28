import logging

from rest_framework.request import Request
from rest_framework.response import Response

from delivery.base_view import BaseView
from . import models
from . import serializers


class MenuListApi(BaseView):

    @staticmethod
    def get(request: Request, *args, **kwargs):
        logging.info(f'query: {request.query_params}')

        restaurant_name = request.query_params.get('restaurant_name')
        restaurant_id = request.query_params.get('restaurant_id')

        query = models.Restaurant.objects
        if restaurant_name:
            query = query.filter(name=restaurant_name)
        if restaurant_id:
            query = query.filter(id=restaurant_id)

        serializer = serializers.MenuSerializer(query, many=True)
        return Response(serializer.data)
