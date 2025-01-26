from rest_framework import serializers
from .models import Transaction


class BuyTransactionSerializer(serializers.ModelSerializer):
    """serializer for endpoint1: buy transaction

    Additional Fields:
        user_id: int: because it was in the document.
    """
    user_id = serializers.IntegerField()
    amount_rial = serializers.IntegerField(min_value=1)

    class Meta:
        model = Transaction
        fields = ["user_id", "amount_rial"]
