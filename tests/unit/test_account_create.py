from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "1234567891", "PROMO_123")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.0
        assert account.pesel == "Invalid"
