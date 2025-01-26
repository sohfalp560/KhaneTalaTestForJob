from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import User, Transaction
from .serializers import BuyTransactionSerializer, SellTransactionSerializer, TransactionSerializer

PRICE_PER_GRAM = 10, 000, 000  # 10,000,000 Rial per gram as document said in different JSONs


class BuyTransactionAPIView(generics.CreateAPIView):
    """Endpoint1"""
    serializer_class = BuyTransactionSerializer

    def perform_create(self, serializer):
        """In the create method this method has been used, so I use it straightly."""
        user_id = serializer.validated_data["user_id"]
        amount_rial = serializer.validated_data["amount_rial"]

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError({"error": "User not found."})

        if user.rial_balance < amount_rial:
            raise ValidationError({"error": "Insufficient Rial balance."})

        gold_weight_gram = amount_rial / PRICE_PER_GRAM

        # Update user balances
        user.rial_balance -= amount_rial
        user.gold_balance += gold_weight_gram
        user.save()

        # Create transaction record
        serializer.save(
            user=user, type="buy", gold_weight_gram=gold_weight_gram, price_per_gram=PRICE_PER_GRAM, status="completed"
        )

class SellTransactionAPIView(generics.CreateAPIView):
    """endpoint2"""
    serializer_class = SellTransactionSerializer

    def perform_create(self, serializer):
        user_id = serializer.validated_data['user_id']
        gold_weight_gram = serializer.validated_data['gold_weight_gram']
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError({"error": "User not found."})

        if user.gold_balance < gold_weight_gram:
            raise ValidationError({"error": "Insufficient gold balance."})

        amount_rial = gold_weight_gram * PRICE_PER_GRAM
        
        # Update user balances
        user.gold_balance -= gold_weight_gram
        user.rial_balance += amount_rial
        user.save()

        # Create transaction record
        serializer.save(
            user=user,
            type='sell',
            amount_rial=amount_rial,
            price_per_gram=PRICE_PER_GRAM,
            status='completed'
        )


class TransactionHistoryAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user_id=user_id)