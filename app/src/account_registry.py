from src.personal_account import PersonalAccount
from pymongo import MongoClient

class AccountRegistry:
    def __init__(self):
        self.accounts = []
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['bank_database']
        self.collection = self.database['accounts']

    def add_account(self, account: PersonalAccount):
        for acc in self.accounts:
            if acc.pesel == account.pesel:
                return False
            
        self.accounts.append(account)
        return True

    def get_accounts(self):
        return self.accounts

    def get_number_of_accounts(self):
        return len(self.accounts)

    def find_account_by_pesel(self, pesel):
        for account in self.accounts:
            if isinstance(account, PersonalAccount) and account.pesel == pesel:
                return account
        return None
    def update_account_data(self, pesel, data_to_change, new_data):
        for account in self.accounts:
            if isinstance(account, PersonalAccount) and account.pesel == pesel and data_to_change in ["first_name", "last_name"]:
                setattr(account, data_to_change, new_data)
                return True
            
        return False
    
    def delete_account(self, pesel):
        for account in self.accounts:
            if isinstance(account, PersonalAccount) and account.pesel == pesel:
                self.accounts.remove(account)
                return True
        
        return False
    
    def load(self):
        self.accounts= []
        for account in self.collection.find({}):
            new_account = PersonalAccount(account["first_name"], account["last_name"], account["pesel"], account["email"])
            new_account.history = account['history']
            new_account.balance = account['saldo']
            self.accounts.append(new_account)

    def save(self):
        self.collection.delete_many({})
        for account in self.accounts:
            self.collection.insert_one({ "first_name": account.first_name, "last_name": account.last_name, "pesel": account.pesel, "email": account.email, "balance": account.balance, "history": account.history })