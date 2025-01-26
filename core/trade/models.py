from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance_Rial = models.PositiveIntegerField(
        default=1000000,
    )
    balance_gold = models.DecimalField(max_digits=12, decimal_places=3, default=0.0)
