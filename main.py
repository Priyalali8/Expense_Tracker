import csv

EXPENSE_FILE = "expenses.csv"
def get_message():
    return "Hello from main.py!"

def add_expense(description, amount, date):
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount,date])

def view_expenses():
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            expenses = view_expenses()
            print("\nRecorded Expenses:")
            for desc, amt in expenses:
                print(f"{desc}: ${amt}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
