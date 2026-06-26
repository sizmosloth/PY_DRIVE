# Expense Tracker with Classes other version is in project folder ---

class Expense :
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
    
    def display(self):
        print(f" - {self.category} - {self.amount} - {self.date}\n")

class ExpenseTracker :
    def __init__(self):
        self.expenses = []

    def add_exp(self, category, amount, date) :
        new = Expense(category, amount, date)
        self.expenses.append(new)
        print(f"Added: {category} - ${amount} - {date}\n")
    
    def view_exp(self):
        if not self.expenses :
            print("No Expenses Yet!\n")
        for i, expense in enumerate(self.expenses):
            print(f"{i + 1}.", end = " ")
            expense.display()
    
    def total_spent(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Spent: ${total}\n")

    def del_exp(self, index):
        self.view_exp()
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed.category} - {removed.amount}\n")
        else :
            print("Invalid Expense Number")

# Using it ---

t = ExpenseTracker()
t.add_exp("Food", 200, "20/06/26")
t.add_exp("Travel", 500, "21/06/26")
t.add_exp("Study", 150, "22/06/26")

t.view_exp()
t.total_spent()
t.del_exp(1)
t.view_exp()
