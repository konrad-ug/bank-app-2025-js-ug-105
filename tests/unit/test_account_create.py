from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestAccount:
    def test_personal_account_creation(self):
        account = PersonalAccount("John", "Doe", "1234567891", "PROM_123")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.0
        assert account.pesel == "Invalid"

    def test_personal_account_creation_valid_PESEL(self):
        account = PersonalAccount("John", "Doe", "12345678901", "PROM_23")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678901"

    def test_company_account_creation_invalid_NIP(self):
        account = CompanyAccount("Microsoft", "12345678910")
        assert account.company_name == "Microsoft"
        assert account.nip == "Invalid"
        assert account.balance == 0.0

    def test_company_account_creation_valid_NIP(self):
        account = CompanyAccount("Microsoft", "1234567890")
        assert account.company_name == "Microsoft"
        assert account.nip == "1234567890"
        assert account.balance == 0.0