from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from src.account import Account

import pytest

class TestAccount:
    def test_account_creation_no_promo_code(self):
        account = Account()
        assert account.balance == 0.0
        assert account.history == []

@pytest.mark.parametrize(
            "name, lastname, pesel, email, promo_code, expected_pesel, expected_balance, expected_history",
            [
                    ["John", "Doe", "1234567890", "email@email.pl", "PROM_123", "Invalid", 0.0, []],
                    ["John", "Doe", "12345678901", "email@email.pl", "PROM_123", "12345678901", 50.0, [50.0]],
                    ["John", "Doe", "87345678901", "email@email.pl", "PROM_123", "87345678901", 50.0, [50.0]],
                    ["John", "Doe", "59125678901", "email@email.pl", "PROM_123", "59125678901", 0.0, []],
            ]
                             )
class TestPersonalAccount:
    def test_personal_account_creation(self, name, lastname, pesel, email, promo_code, expected_pesel, expected_balance, expected_history):
        account = PersonalAccount(name, lastname, pesel, email, promo_code)
        assert account.first_name == name
        assert account.last_name == lastname
        assert account.pesel == expected_pesel
        assert account.email == email
        assert account.balance == expected_balance
        assert account.express_loan_fee == 1.0
        assert account.history == expected_history

@pytest.mark.parametrize(
            "name, nip, email, expected_nip, expected_balance, expected_history",
            [
                    ["Company Name", "12345678910", "email@email.pl", "Invalid", 0.0, []],
                    ["Company Name", "1234567890", "email@email.pl", "1234567890", 0.0, []],
            ]
                             )
class TestCompanyAccount:
    def test_company_account_creation(self, name, nip, email, expected_nip, expected_balance, expected_history):
        account = CompanyAccount(name, nip, email)
        assert account.company_name == name
        assert account.nip == expected_nip
        assert account.email == email
        assert account.balance == expected_balance
        assert account.express_loan_fee == 5.0
        assert account.history == expected_history