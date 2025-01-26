from django.urls import path
from .apis import BuyTransactionAPIView

urlpatterns = [
    path('buy/', BuyTransactionAPIView.as_view(), name='buy-transaction'),
]
