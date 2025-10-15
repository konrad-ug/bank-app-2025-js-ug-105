import re
import datetime

class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50.0 if self.provided_promo_code(promo_code) else 0.0
        self.pesel = pesel if self.is_PESEL_valid(pesel) else "Invalid"



    def is_PESEL_valid(self, pesel):
        if pesel and len(pesel) == 11:
            return True
        return False

    def provided_promo_code(self, promo_code):
        if promo_code and re.search("^PROM_...$", promo_code):
            return True
        return False