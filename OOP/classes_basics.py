# classes & objects in python ---

# classes are the blueprint and objects are actual thing

class Expense:
    def __init__(self, category, amount, date):
        self.catgory = category
        self.amount = amount
        self.date = date
    # this runs automatically everytime new expense is being create

    def display(self):
        print(f" - {self.category} - {self.amount} - {self.date}")

# creating actual objects (instances) from the blueprint
e1 = Expense("Food", 200, "20/06/26")
e2 = Expense("Travel", 500, "21/06/26")

e1.display()
e2.display()

print(e1.category)
print(e2.date)

# __init__ = "initialize" means it runs once object is created as a constructor in c++
# self     = a specifi object lets each expense remember its own details

e3 = Expense("Entertainment", 900, "13/06/26")