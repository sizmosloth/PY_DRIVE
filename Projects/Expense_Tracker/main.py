# Expenses Tracker for User --->

expenses = []

def add_expense(ammount, category, date):
    exp = {
        "Ammount" : ammount,
        "Category" : category,
        "Date" : date
    }
    expenses.append(exp)
    print(f"Expense added of category : {category} of ${ammount} on date(DD/MM/YY): {date}")

def all_exp():
    if not expenses:
        print("NO EXPENSES YET!!!")
        return
    for i, expense in enumerate(expenses):
        print(f"{i + 1} - {expense['Category']} - ${expense['Ammount']} - {expense['Date']}")
    
# Manual Testing

add_expense(500, "Food", "06/12/26")
all_exp()