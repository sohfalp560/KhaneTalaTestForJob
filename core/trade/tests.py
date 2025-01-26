from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model() # for get user data to test


class TransactionTests(TestCase):
    """Because I want to show my ability to develop with TDD: test-driven development.

    Tests:
        Buy gold
        Sell gold
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpass", rial_balance=10000000, gold_balance=1.0
        )

    def test_buy_gold(self):
        data = {"user_id": self.user.id, "amount_rial": 5000000}
        response = self.client.post("/transactions/buy/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user.refresh_from_db()
        self.assertEqual(self.user.rial_balance, 5000000)
        self.assertAlmostEqual(self.user.gold_balance, 1.5)

    def test_sell_gold(self):
        data = {'user_id': self.user.id, 'gold_weight_gram': 0.5}
        response = self.client.post('/transactions/sell/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user.refresh_from_db()
        self.assertEqual(self.user.rial_balance, 10000000 + 5000000)
        self.assertAlmostEqual(self.user.gold_balance, 0.5)