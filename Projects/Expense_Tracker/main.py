# Expenses Tracker for User --->

expenses = []

def add_expense(**details):
    expenses.append(details)
    print(f"Expense added of category : {details['Category']} of ${details['Ammount']} on date(DD/MM/YY): {details['Date']}\n")

def all_exp():
    if not expenses:
        print("NO EXPENSES YET!!!")
        return
    for i, expense in enumerate(expenses):
        print(f"{i + 1} - {expense['Category']} - ${expense['Ammount']} - {expense['Date']}\n")
    
def total_spent():
    if not expenses:
        print("NO EXPENSES YET!!!")
        return
    total = 0
    for i in expenses:
        total = total + int(i['Ammount'])
    print(f"Total Spent is : ${total}\n")
# Manual Testing

add_expense(Ammount = 500, Category = "Food", Date = "03/06/26")
all_exp()
total_spent()