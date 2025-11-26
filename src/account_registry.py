from src.personal_account import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def get_number_of_accounts(self):
        return len(self.accounts)

    def find_account_by_pesel(self, pesel):
        for account in self.accounts:
            if isinstance(account, PersonalAccount) and account.pesel == pesel:
                return account
        return None