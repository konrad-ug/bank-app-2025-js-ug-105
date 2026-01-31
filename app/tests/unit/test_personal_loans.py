import pytest

from src.personal_account import PersonalAccount

class TestLoans:
    @pytest.fixture
    def account(self):
        return PersonalAccount("John", "Doe", "12345678901", "email@email.pl",)
        
    def test_submit_for_loan_insufficient_transactions(self, account):
        account.balance = -30.0
        account.outgoing_transfer(100.0)
        account.incoming_transfer(150.0)
        assert account.balance == 120.0
        assert account.history == [150.0]
        account.submit_for_loan(150)
        assert account.balance == 120.0

    def test_submit_for_loan_insufficient_income(self, account):
        account.balance = 49.0
        account.history = [-100.0, -1.0, 150.0]
        account.submit_for_loan(150.0)
        assert account.balance == 49.0


    def test_submit_for_loan_sufficient_income(self, account):
        account.balance = 200.0
        account.history = [100.0, 50.0, 20.0, 10.0, 20.0]
        account.submit_for_loan(150.0)
        assert account.balance == 350.0

    def test_submit_for_loan_sufficient_income_balance(self, account):
        account.balance = 40.0
        account.history = [100.0, -50.0, 20.0, -10.0, -20.0]
        account.submit_for_loan(10.0)
        assert account.balance == 50.0

    def test_submit_for_loan_insufficient_income_balance(self,account):
        account.balance = 40.0
        account.history = [100.0, -50.0, 20.0, -10.0, -20.0]
        print(sum(account.history))
        account.submit_for_loan(50.0)
        assert account.balance == 40.0