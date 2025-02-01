class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable! Cannot withdraw more than the current balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")


acc = Account("Bruce Banner", 500)
acc.deposit(200)
acc.withdraw(1000)
acc.withdraw(300)