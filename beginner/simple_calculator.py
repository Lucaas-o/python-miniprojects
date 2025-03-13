def select_operation():
    print("\nPlease select an operation (number or symbol):")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    operation = input("Enter choice: ").strip()

    if operation in ["5", "exit"]:
        return "Exit"

    if operation not in ["1", "2", "3", "4", "+", "-", "*", "/"]:
        print("Invalid operation. Please try again.")
        return None

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input. Please enter valid numbers.")
        return None

    if operation in ["1", "+"]:
        return num1 + num2
    elif operation in ["2", "-"]:
        return num1 - num2
    elif operation in ["3", "*"]:
        return num1 * num2
    elif operation in ["4", "/"]:
        return num1 / num2 if num2 != 0 else "Error: Division by zero"

def main():
    while True:
        result = select_operation()
        if result == "Exit":
            print("Goodbye!")
            break
        elif result is not None:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
