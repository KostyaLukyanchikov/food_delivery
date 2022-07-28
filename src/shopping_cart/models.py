import logging

from django.db import models

from menu import models as menu_models


class CartPosition(models.Model):
    dish = models.OneToOneField(
        to=menu_models.Dish,
        to_field='id',
        on_delete=models.CASCADE,
        primary_key=True
    )
    quantity = models.IntegerField(null=False)

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):
        try:
            position = CartPosition.objects.get(dish=self.dish)
            position.quantity += self.quantity
            logging.info(f'increasing position {position.dish} quantity')
            super(CartPosition, position).save()

        except CartPosition.DoesNotExist:
            logging.info('saving cart position')
            super(CartPosition, self).save()

    @staticmethod
    def delete_position(dish: int, quantity: int):
        try:
            position = CartPosition.objects.get(dish=dish)
            position.quantity -= quantity

            if position.quantity > 0:
                logging.info(f'cutting position {position.dish} quantity')
                super(CartPosition, position).save()
                return

            logging.info('deleting whole position')
            super(CartPosition, position).delete()

        except CartPosition.DoesNotExist:
            logging.info('position not in cart')
