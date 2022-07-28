from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=False, auto_now_add=True)
    price = models.FloatField(null=False)

    def __repr__(self):
        return f'Order(id={self.id}, time={self.time})'


class OrderPosition(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=False)
    order = models.ForeignKey(
        to=Order,
        to_field='id',
        on_delete=models.CASCADE,
        related_name='positions',
        null=True
    )

    # consider not to use dish as foreign key,
    # case changing the dish could possibly change already made orders
    dish_id = models.IntegerField(null=False)
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField()

    def __repr__(self):
        return (
            f'OrderPosition('
            f'id={self.id}, '
            f'name={self.name}, '
            f'price={self.price}, '
            f'quantity={self.quantity}, '
            f'order={self.order}'
            f')'
        )
