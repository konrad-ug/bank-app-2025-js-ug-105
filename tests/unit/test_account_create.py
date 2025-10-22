from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestAccount:
    def test_personal_account_creation(self):
        account = PersonalAccount("John", "Doe", "1234567891", "PROM_123")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.0
        assert account.pesel == "Invalid"

    def test_company_account_creation(self):
        account = CompanyAccount("Microsoft", "12345678910")
        assert account.company_name == "Microsoft"
        assert account.nip == "Invalid"
        assert account.balance == 0.0