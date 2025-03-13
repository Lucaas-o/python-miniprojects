import json
import os
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.json")

class ExpenseTracker:
    def __init__(self, filename=EXPENSES_FILE):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, name, price, date=None):
        expense = {
            "id": len(self.expenses) + 1,
            "name": name,
            "price": float(price),
            "date": date
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense added: {name}.")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("--- Your Expenses ---")
            for expense in self.expenses:
                print(f"{expense['id']}. {expense['name']} - ${expense['price']} (Date: {expense['date']})")
            print("---------------------")

    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                print(f"Expense {expense_id} removed.")
                return
        print(f"Expense with ID {expense_id} not found.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        return None

def main():
    tracker = ExpenseTracker()
    while True:
        clear_screen()
        print("--- Expenses Tracker ---")
        print("1. Show expenses")
        print("2. Add expense")
        print("3. Remove expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            clear_screen()
            tracker.show_expenses()
            time.sleep(2)
        elif choice == "2":
            clear_screen()
            name = input("Product name: ")
            while True:
                price = input("Price: ")
                try:
                    float(price)
                    break
                except ValueError:
                    print("Invalid price. Enter a valid number.")
            date = input("Purchase date (DD-MM-YYYY, optional): ") or None
            if date and not validate_date(date):
                print("Invalid date format. Date will be ignored.")
                date = None
            tracker.add_expense(name, price, date)
            time.sleep(2)
        elif choice == "3":
            clear_screen()
            tracker.show_expenses()
            try:
                expense_id = int(input("Expense ID to remove: "))
                tracker.remove_expense(expense_id)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            time.sleep(2)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
