expenses = []

def add_expense():
    date = input("Enter date (dd-mm-yyyy): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    desc = input("Enter description: ")
    entry = [date, amount, category, desc]
    expenses.append(entry)
    print("Expense added!")

def show_expenses():
    print("\nAll Expenses:")
    for entry in expenses:
        print("Date:", entry[0], "| Amount:", entry[1], "| Category:", entry[2], "| Description:", entry[3])

def show_total():
    total = 0
    for entry in expenses:
        total += entry[1]
    print("Total Expenses:", total)

while True:
    print("\n1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


