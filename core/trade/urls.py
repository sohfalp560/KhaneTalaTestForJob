from django.urls import path
from .apis import BuyTransactionAPIView, SellTransactionAPIView

urlpatterns = [
    path('buy/', BuyTransactionAPIView.as_view(), name='buy-transaction'),
    path('sell/', SellTransactionAPIView.as_view(), name='sell-transaction'),
]
