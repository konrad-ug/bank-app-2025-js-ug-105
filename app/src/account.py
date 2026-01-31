from datetime import datetime
from src.smtp.smtp import SMTPClient 

class Account:

    def __init__(self):
        self.balance = 0.0
        self.history = []
        self.express_loan_fee = 0.0
        self.email = ""
        self.account_type = None

    def outgoing_transfer(self, amount, express=False):
        if self.sufficient_balance(amount):
            self.balance -= amount
            self.history.append(-amount)
            if express:
                self.balance -= self.express_loan_fee
                self.history.append(-self.express_loan_fee)
            return True
        return False
        

    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)
            return True
        return False

    def sufficient_balance(self, amount):
        if 0 < amount <= self.balance:
            return True

        return False
    
    def send_history_via_email(self, email_adress):
        text = f"{self.account_type} account history: {self.history}"
        date = datetime.now().date()
        subject = f"Account Transfer History {date}"
        return SMTPClient.send(subject, text, email_adress)