from src.personal_account import PersonalAccount


class TestTransfers:
    def test_outgoing_sufficient_balance(self):
        account = PersonalAccount("John", "Doe", "1234567891")
        account.balance = 100.0
        account.outgoing_transfer(100.0)
        account.incoming_transfer(150.0)
        assert account.balance == 150.0
    
    def test_outgoing_insufficient_balance(self):
        account = PersonalAccount("John", "Doe", "1234567891")
        account.balance = -30.0
        account.outgoing_transfer(100.0)
        account.incoming_transfer(150.0)
        assert account.balance == 120.0