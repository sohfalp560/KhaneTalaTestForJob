from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Create custom user account system with AbstractUser from djnago 

    Additional Fields:
        balance_Rial: positive_integer: as balance of user in Rial (cash) as I write default value is 100 Toman.
        balance_gold: decimal: as balance of user in gold (gram) from 0.001 to 1,000,000,000
    """
    balance_Rial = models.PositiveIntegerField(
        default=1000000,
    )
    balance_gold = models.DecimalField(max_digits=12, decimal_places=3, default=0.0)


class Transaction(models.Model):
    """Transaction Model for saving in database.

    Fields:
        user: Foreign_key: relating user with this model.
        type: char: choices from TypeOfTX as Buy, Sell
        amount_rial: int: cash to pay or give in Rial
        gold_weight_gram: decimal: gold gram to pay or equal to cash (Rial)
        price_per_gram: positive_integer: price of gold Rial/Gram.
        status: char: choices for transaction state: is it pending? or completed? or unfortunately gives error?
    """
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
