from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        self.balance = 0.0
        self.company_name = company_name
        self.nip = nip if self.is_NIP_valid(nip) else "Invalid"
        self.history = []
        self.express_loan_fee = 5.0

    def submit_for_loan(self, amount):
        if self.can_submit_for_loan(amount):
            self.balance += amount
            return True
        return False

    def can_submit_for_loan(self, amount):
        if self.balance*2 > amount and 1775.0 in self.history:
            return True
        return False

    def is_NIP_valid(self, nip):
        if nip and len(nip) == 10:
            return True
        return False