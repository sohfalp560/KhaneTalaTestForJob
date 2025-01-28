# Gold Trade API
This project is a Django-based API for managing gold transactions, including buying and selling gold, and viewing transaction history. It is designed to handle user balances in both Rial (currency) and gold (grams), and ensures proper validation and error handling.

---

## **Goal**

The goal of this project is to provide a simple and efficient API for managing gold transactions. Users can:
1. **Buy gold** by spending Rial.
2. **Sell gold** to receive Rial.
3. **View their transaction history**.

The API ensures that:
- Users cannot spend more Rial than they have.
- Users cannot sell more gold than they own.
- All transactions are recorded and can be retrieved for historical purposes.

---

## **Features**

- **User Management**:
  - Custom `User` model with balances for Rial and gold.
- **Transaction Management**:
  - Buy gold using Rial.
  - Sell gold to receive Rial.
  - View transaction history for a user.
- **Validation**:
  - Prevents invalid transactions (e.g., insufficient balance).
- **Testing**:
  - Test-driven development (TDD) with unit tests for all endpoints.
- **Documentation**:
  - Clear API documentation in the `README.md` file.

---

## **Setup**

### Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework

### Installation
1. Using **uv**:
   ```bash
   pip install uv
   ```
   ```bash
   uv sync
   ```
   And when you gonna run manage.py:
   ```bash
   uv run core/manage.py ...
   ```

2. Using **virtualenv**:
   ```bash
   virtualenv .venv
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## **API Endpoints**

### 1. **Buy Gold**
- **Endpoint**: `POST /transactions/buy/`
- **Request Body**:
  ```json
  {
    "user_id": 1,
    "amount_rial": 5000000
  }
  ```
- **Response**:
  ```json
  {
    "transaction_id": 101,
    "user_id": 1,
    "amount_rial": 5000000,
    "gold_weight_gram": 0.5,
    "price_per_gram": 10000000,
    "status": "completed"
  }
  ```

### 2. **Sell Gold**
- **Endpoint**: `POST /transactions/sell/`
- **Request Body**:
  ```json
  {
    "user_id": 1,
    "gold_weight_gram": 0.5
  }
  ```
- **Response**:
  ```json
  {
    "transaction_id": 102,
    "user_id": 1,
    "gold_weight_gram": 0.5,
    "amount_rial": 5000000,
    "price_per_gram": 10000000,
    "status": "completed"
  }
  ```

### 3. **View Transaction History**
- **Endpoint**: `GET /transactions/user/<user_id>/`
- **Response**:
  ```json
  [
    {
      "transaction_id": 101,
      "type": "buy",
      "amount_rial": 5000000,
      "gold_weight_gram": 0.5,
      "price_per_gram": 10000000,
      "date": "2025-01-11T12:34:56Z",
      "status": "completed"
    },
    {
      "transaction_id": 102,
      "type": "sell",
      "amount_rial": 5000000,
      "gold_weight_gram": 0.5,
      "price_per_gram": 10000000,
      "date": "2025-01-12T12:34:56Z",
      "status": "completed"
    }
  ]
  ```

---

## **Testing**

The project includes unit tests to ensure the functionality works as expected. To run the tests:

```bash
python manage.py test transactions
```

### Test Coverage
- **Buy Gold**: Validates Rial balance and gold weight calculations.
- **Sell Gold**: Validates gold balance and Rial calculations.

---

## **Dummy Data**

To populate the database with dummy data for testing and development, use the `django-extensions` script:

1. **Install `django-extensions`**:
   ```bash
   pip install django-extensions
   ```

2. **Run the script**:
   ```bash
   python manage.py runscript create_dummy_data --script-args transactions
   ```

This will create:
- Two users with initial balances.
- Sample buy and sell transactions.

---

## **Project Structure**

```
gold_api/
├── gold_api/                  # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── transactions/              # Transactions app
│   ├── __init__.py
│   ├── models.py              # User and Transaction models
│   ├── serializers.py         # Serializers for API requests/responses
│   ├── apis.py                # API views
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App-specific URLs
│   └── scripts/               # Scripts for dummy data
│       └── create_dummy_data.py
└── README.md                  # Project documentation
```

---

## **Technologies Used**

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **SQLite**: Default database for development.
- **django-extensions**: For running custom scripts.

---

Thank you for using the Gold Transaction API! 🚀