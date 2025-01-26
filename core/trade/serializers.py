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

class SellTransactionSerializer(serializers.ModelSerializer):
    """serializer for endpoint2: sell transaction

    Additional Fields:
        user_id: int: because it was in the document.
    """
    user_id = serializers.IntegerField()
    gold_weight_gram = serializers.FloatField(min_value=0.001)

    class Meta:
        model = Transaction
        fields = ['user_id', 'gold_weight_gram']