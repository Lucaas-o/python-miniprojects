import json
import os
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(name, price, date=None):
    new_expense = {
        "id": len(expenses) + 1,
        "name": name,
        "price": float(price),
        "date": date
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"\nExpense added: {name}.")

def show_expenses():
    if not expenses:
        print("\nNo expenses found.")
    else:
        print("\n--- Your Expenses ---")
        for expense in expenses:
            print(f"{expense['id']}. {expense['name']} - ${expense['price']} (Date: {expense['date']})")
        print("--------------------")

def remove_expense(product_id):
    global expenses
    expense_found = False
    for expense in expenses:
        if expense["id"] == product_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print(f"\nExpense {product_id} removed.")
            expense_found = True
            break
    if not expense_found:
        print(f"\nExpense with ID {product_id} not found.")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_date(date_str):
    """
    Validates if the date is in the correct format (DD-MM-YYYY).
    Args:
        date_str (str): The date string to validate.
    Returns:
        str: The validated date string, or None if invalid.
    """
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        return None

def main():
    global expenses
    expenses = load_expenses()

    while True:
        clear_screen()  # Clear the terminal screen
        print("\n--- Expenses Tracker ---")
        print("1. Show expenses")
        print("2. Add expense")
        print("3. Remove expense")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_expenses()
            input("\nPress Enter to continue...")  # Pause before clearing the screen
        elif choice == "2":
            name = input("Enter the name of the product: ")
            while True:
                price = input("Enter the price of the product: ")
                try:
                    float(price)  # Validate if the price is a valid number
                    break
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
            date = input("Enter the date of the purchase (DD-MM-YYYY, optional): ") or None
            if date:
                validated_date = validate_date(date)
                if not validated_date:
                    print("Invalid date format. Date will be ignored.")
                    date = None
            add_expense(name, price, date)
            input("\nPress Enter to continue...")  # Pause before clearing the screen
        elif choice == "3":
            show_expenses()  # Show the list of expenses before asking for the ID
            try:
                product_id = int(input("\nEnter the ID of the product to remove: "))
                remove_expense(product_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
            input("\nPress Enter to continue...")  # Pause before clearing the screen
        elif choice == "4":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")  # Pause before clearing the screen

if __name__ == "__main__":
    main()