from random import randint, randrange
from trade.models import User, Transaction

"""I want to delete this file and strategy but I think you can see it.
code: python manage.py runscript create_dummy_data
"""

def run():
    # Create dummy users
    user0 = User.objects.create_user(
        username='testuser',
        password='testpass',
        rial_balance=randrange(1000000,100000000),
        gold_balance=0.0
    )
    user1 = User.objects.create_user(
        username='testuser1',
        password='testpass',
        rial_balance=randrange(1000000,100000000),
        gold_balance=2.0
    )

    # Create dummy transactions
    Transaction.objects.create(
        user=user0,
        type='buy',
        amount_rial=5000000,  # 5,000,000 Rial
        gold_weight_gram=0.5,  # 0.5 grams of gold
        price_per_gram=10000000,  # 10,000,000 Rial per gram
        status='completed'
    )
    Transaction.objects.create(
        user=user1,
        type='sell',
        amount_rial=10000000,  # 10,000,000 Rial
        gold_weight_gram=1.0,  # 1 gram of gold
        price_per_gram=10000000,  # 10,000,000 Rial per gram
        status='completed'
    )

    print("Dummy data created successfully!")