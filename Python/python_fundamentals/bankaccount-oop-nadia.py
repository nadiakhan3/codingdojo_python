class BankAccount:
    def __init__(self, rate, balance=0):
        self.int_rate = (rate * .01)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_balance(self):
        print(self.balance)
    
    def yield_interest(self):
        self.balance * self.int_rate

moneybb = BankAccount(.05, 2000)
print (moneybb.balance)

moneybb2 = BankAccount(5, 4000)
print(moneybb2.balance)
print(moneybb2.display_balance)


moneybb.deposit(3000).deposit(500).deposit(300).withdraw(1000).yield_interest().display_balance()