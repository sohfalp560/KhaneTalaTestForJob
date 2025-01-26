from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance_Rial = models.PositiveIntegerField(
        default=1000000,
    )
    balance_gold = models.DecimalField(max_digits=12, decimal_places=3, default=0.0)


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = "pn", "on Pending"
        COMPLETED = "cm", "Completed!"
        ERROR = "er", "Error!"

    class TypeOfTX(models.TextChoices):
        BUY = "B", "Buy Transaction"
        SELL = "S", "Buy Transaction"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=1,
        choices=TypeOfTX,
        null=False,
        blank=False,
    )
    amount_rial = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    gold_weight_gram = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        null=False,
        blank=False,
    )
    price_per_gram = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.PENDING,
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} by User {self.user_id}"
