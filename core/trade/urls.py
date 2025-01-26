from django.urls import path
from .apis import BuyTransactionAPIView, SellTransactionAPIView, TransactionHistoryAPIView

urlpatterns = [
    path('buy/', BuyTransactionAPIView.as_view(), name='buy-transaction'),
    path('sell/', SellTransactionAPIView.as_view(), name='sell-transaction'),
    path('user/<int:user_id>/', TransactionHistoryAPIView.as_view(), name='transaction-history'),
]
