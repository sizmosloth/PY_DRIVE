# INHERITANCE — ONE CLASS BUILDING ON ANOTHER

# inheritance = "this new class is basically that other class,
#                plus a few extra things"

# THE PARENT CLASS (also called the "base class")

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def display(self):
        print(f"{self.category} - ${self.amount} - {self.date}")

# THE CHILD CLASS — INHERITS everything from Expense

class RecurringExpense(Expense):   # ← this is the inheritance part
    def __init__(self, category, amount, date, frequency):
        super().__init__(category, amount, date)
        # super() means "run the PARENT's __init__ first"
        # so we don't have to rewrite self.category = category, etc.
        self.frequency = frequency   # this is the NEW thing only RecurringExpense has

    # OVERRIDING — same method name, but a different version for this child
    def display(self):
        print(f"{self.category} - ${self.amount} - {self.date} (repeats: {self.frequency})")

e1 = Expense("Food", 200, "20/06/26")
e2 = RecurringExpense("Netflix", 15, "01/06/26", "monthly")
e1.display()   # Food - $200 - 20/06/26
e2.display()   # Netflix - $15 - 01/06/26 (repeats: monthly)
# notice: each one used ITS OWN version of display()
# this is called "method overriding"

# isinstance — checking what something actually is
print(isinstance(e2, RecurringExpense))   # True
print(isinstance(e2, Expense))            # ALSO True — e2 IS an Expense too
print(isinstance(e1, RecurringExpense))   # False — e1 is just a plain Expense

# A LIST CAN HOLD BOTH TYPES TOGETHER — THIS IS THE REAL POWER

all_expenses = [
    Expense("Food", 200, "20/06/26"),
    RecurringExpense("Netflix", 15, "01/06/26", "monthly"),
    Expense("Travel", 500, "21/06/26"),
    RecurringExpense("Gym", 30, "01/06/26", "monthly"),
]

for exp in all_expenses:
    exp.display()
    # python automatically calls the RIGHT version of display()
    # for each object — you don't need an if/elif checking the type
    # this automatic behavior is called POLYMORPHISM