class Account:

    def __init__(self):
        self.balance = 0.0

    def outgoing_transfer(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        

    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount