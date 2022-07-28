from django.db import models


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField()
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='dishes',
        on_delete=models.CASCADE
    )
