class Account:

    def __init__(self):
        self.balance = 0.0
        self.history = []
        self.express_loan_fee = 0.0

    def outgoing_transfer(self, amount, express=False):
        if self.sufficient_balance(amount):
            self.balance -= amount
            self.history.append(-1 * amount)
        if express:
            self.balance -= (amount + self.express_loan_fee)
            self.history.append(-1 * self.express_loan_fee)
        

    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def sufficient_balance(self, amount):
        if 0 < amount <= self.balance:
            return True

        return False