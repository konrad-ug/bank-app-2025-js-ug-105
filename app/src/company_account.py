from src.account import Account
import requests
import os
from datetime import datetime

class CompanyAccount(Account):
    def __init__(self, company_name, nip, email):
        self.balance = 0.0
        self.company_name = company_name
        self.email = email
        
        if len(nip) == 10:
            if self.check_NIP_with_API(nip):
                self.nip = nip
            else:
                raise ValueError("Company not registered!!")
        else:
            self.nip = "Invalid"

        self.history = []
        self.express_loan_fee = 5.0
        self.account_type = "Company"

    def submit_for_loan(self, amount):
        if self.can_submit_for_loan(amount):
            self.balance += amount
            return True
        return False

    def can_submit_for_loan(self, amount):
        if self.balance*2 > amount and 1775.0 in self.history:
            return True
        return False

    def check_NIP_with_API(self, nip):
        url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        date = datetime.now().date()
        nip_url = f"{url}api/search/nip/{nip}?date={date}"
        response = requests.get(nip_url)
        print(f"Response: {response.status_code}, {response.json()}")
        return response.status_code == 200

