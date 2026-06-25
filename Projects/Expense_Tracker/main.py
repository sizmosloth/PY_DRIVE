# Expenses Tracker for User --->
import json

filename = "expenses.json" 

expenses = []

def save_expenses():
    with open (filename, "w") as f:
        json.dump(expenses, f, indent = 4)

def load_expenses():
    global expenses
    try:
        with open(filename, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def add_expense(**details):
    expenses.append(details)
    print(f"Expense added of category : {details['Category']} of ${details['Ammount']} on date(DD/MM/YY): {details['Date']}\n")
    save_expenses()

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
        total = total + float(i['Ammount'])
    print(f"Total Spent is : ${total}\n")

def filter_by_category(cat):
    found = False

    for expense in expenses:
        if expense['Category'] == cat:
            print(f"- {expense['Category']} - ${expense['Ammount']} - {expense['Date']}")
            found = True
    if not found:
        print("No Category Found!")

def delete_expense(index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['Category']} - ${removed['Ammount']}\n")
        save_expenses()
    else:
        print("Invalid expense number")

# Main Menu

def main():
    load_expenses() # Loads save data the moment app starts ---
    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Total spent")
        print("4. Filter by category")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = input("Amount: ")
            date = input("Date (DD/MM/YY): ")
            add_expense(Category=category, Ammount=amount, Date=date)
        elif choice == "2":
            all_exp()

        elif choice == "3":
            total_spent()

        elif choice == "4":
            cat = input("Enter category to filter: ")
            filter_by_category(cat)

        elif choice == "5":
            all_exp()
            num = int(input("Enter expense number to delete: "))
            delete_expense(num - 1)

        elif choice == "6":
            print("Bye!")
            break

        else:
            print("Invalid choice, try again")
    
if __name__ == "__main__":
    main()