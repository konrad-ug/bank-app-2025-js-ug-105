from src.account import Account

import re
import datetime

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, email, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel if self.is_PESEL_valid(pesel) else "Invalid"
        self.email = email
        self.history = []
        self.express_loan_fee = 1.0
        self.account_type = "Personal"

        if self.provided_promo_code(promo_code) and self.is_qualified_for_promo_code(pesel):
            self.balance = 50.0
            self.history.append(50.0)
        else:
            self.balance = 0.0


    def submit_for_loan(self, amount):
        if self.can_submit_for_loan(amount):
            self.balance += amount
            return True
        return False

    def can_submit_for_loan(self, amount):
        if len(self.history) >= 3 and (self.history[-1] > 0.0 and self.history[-2] > 0.0 and self.history[-3] > 0.0):
            return True
        elif len(self.history) >= 5 and self.history[-1] + self.history[-2] + self.history[-3]  + self.history[-4] + self.history[-5] > amount:
            return True

        return False

    def is_PESEL_valid(self, pesel):
        if pesel and len(pesel) == 11 and re.search("^[0-9]*$", pesel):
            return True
        return False

    def provided_promo_code(self, promo_code):
        if promo_code and re.search("^PROM_...$", promo_code):
            return True
        return False
    
    def is_qualified_for_promo_code(self, pesel):
        if not self.is_PESEL_valid(pesel):
            return False
        if int(pesel[0:2]) > 60:
            return True
        elif int(pesel[2:4]) > 20:
            return True
        return False