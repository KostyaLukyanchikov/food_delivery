from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q


class CustomUser(AbstractUser):
    balance = models.FloatField(null=True, default=1000)

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(balance__gte=0.0),
                name='balance_is_positive'),
        )
