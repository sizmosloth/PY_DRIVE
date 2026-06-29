# ENCAPSULATION — PROTECTING DATA INSIDE A CLASS

# right now, anyone can do this and break your data:
#   tracker.expenses = "oops i broke it"
# encapsulation = controlling HOW data gets read/changed

class mybank:
    def __init__(self, balance):
        self._balance = balance
        # the underscore before balance tells other programmers to not touch balance directly use the proper function instead
        # it is convection not a hard rule
        # it trust programmers (*trust Programmers*) that they won't do anything what they are said not to do WOW.

    def deposit(self, amount):
        if amount <= 0 :
            print(f"Cannot Deposite ${amount}.\n")
            return
        self._balance += amount
        print(f"Deposited ${amount}.\n")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient Funds.\n")
        self._balance -= amount
        print(f"Withdrew ${amount}\n")

    def get_balance(self):
        print(f"Available Funds in Account ${self._balance}.\n")

account = mybank(5000)
account.deposit(500)
account.deposit(700)
account.deposit(10)
account.deposit(70000)
account.withdraw(10000)
account.get_balance()


# without encapsulation, someone could do this and break everything:
account._balance = -99999   # technically still possible (Python doesn't FULLY lock it)
# but the underscore is a clear signal: "you're not supposed to do this"


# Like in c++ we can use private for our variables so they cant get modified directly
# Py is some different lvl shit, it has

# @property — A CLEANER WAY TO CONTROL ACCESS

