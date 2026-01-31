from src.company_account import CompanyAccount  
import pytest

@pytest.fixture
def account():
    return CompanyAccount("TechCorp", "1234567890", "email@email.pl")

class TestBusinessLoans:
    name = "JOG"
    nip = "8461627563"
    wrong_nip = "7461617563"

    def test_submit_for_loan_insufficient_balance(self, account):
        account.balance = 500.0
        account.history = [1775]
        account.submit_for_loan(1200.0)
        assert account.balance == 500.0

    def test_submit_for_loan_missing_history(self, account):
        account.balance = 2000.0
        account.history = []
        account.submit_for_loan(1500.0)
        assert account.balance == 2000.0

    def test_submit_for_loan_sufficient_balance_and_history(self, account):
        account.balance = 2000.0
        account.history = [1775, 3000.0]
        account.submit_for_loan(1500.0)
        assert account.balance == 3500.0