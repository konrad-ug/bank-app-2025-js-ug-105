from src.company_account import CompanyAccount

class TestBusinessLoans:
    def test_submit_for_loan_insufficient_balance(self):
        account = CompanyAccount("TechCorp", "1234567890")
        account.balance = 500.0
        account.history = [1775]
        account.submit_for_loan(1200.0)
        assert account.balance == 500.0

    def test_submit_for_loan_missing_history(self):
        account = CompanyAccount("TechCorp", "1234567890")
        account.balance = 2000.0
        account.history = []
        account.submit_for_loan(1500.0)
        assert account.balance == 2000.0

    def test_submit_for_loan_sufficient_balance_and_history(self):
        account = CompanyAccount("TechCorp", "1234567890")
        account.balance = 2000.0
        account.history = [1775, 3000.0]
        account.submit_for_loan(1500.0)
        assert account.balance == 3500.0