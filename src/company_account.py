from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        self.balance = 0.0
        self.company_name = company_name
        self.nip = nip if self.is_NIP_valid(nip) else "Invalid"

    def is_NIP_valid(self, nip):
        if nip and len(nip) == 10:
            return True
        return False