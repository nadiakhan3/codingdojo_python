class User:
    def __init__(self, name):
        self.name = name 
        self.account_balance = 0


    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Balance: ${self.account_balance}")
        return self


guido = User("Guido van Rossum")
nadia = User("Nadia Testing")
jack= User("Jackie Johnson")
print(guido.name)

guido.make_deposit(10000)
print(guido.account_balance)

guido.make_withdrawal(5000)
print(guido.make_withdrawal)

guido.display_user_balance()

guido.make_deposit(675)
guido.make_deposit(120)
guido.make_withdrawal(213)
guido.display_user_balance()

guido.make_deposit(600).make_deposit(120).make_withdrawal(213).display_user_balance()
