def convert_length(value, from_unit, to_unit):
    if from_unit == "meters" and to_unit == "feet":
        return value * 3.28084
    elif from_unit == "feet" and to_unit == "meters":
        return value / 3.28084
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    if from_unit == "kilograms" and to_unit == "pounds":
        return value * 2.20462
    elif from_unit == "pounds" and to_unit == "kilograms":
        return value / 2.20462
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    else:
        return None

def get_conversion_choice():
    print("Select the type of conversion:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    choice = input("Enter the number of your choice: ")
    return choice

def main():
    while True:
        choice = get_conversion_choice()

        try:
            if choice == "1":
                value = float(input("Enter value: "))
                from_unit = input("From (meters/feet): ").lower()
                to_unit = input("To (meters/feet): ").lower()
                result = convert_length(value, from_unit, to_unit)
                if result is None:
                    print("Invalid units for length conversion.")
                else:
                    print(f"{value} {from_unit} = {result} {to_unit}")
            elif choice == "2":
                value = float(input("Enter value: "))
                from_unit = input("From (kilograms/pounds): ").lower()
                to_unit = input("To (kilograms/pounds): ").lower()
                result = convert_weight(value, from_unit, to_unit)
                if result is None:
                    print("Invalid units for weight conversion.")
                else:
                    print(f"{value} {from_unit} = {result} {to_unit}")
            elif choice == "3":
                value = float(input("Enter value: "))
                from_unit = input("From (Celsius/Fahrenheit): ").lower()
                to_unit = input("To (Celsius/Fahrenheit): ").lower()
                result = convert_temperature(value, from_unit, to_unit)
                if result is None:
                    print("Invalid units for temperature conversion.")
                else:
                    print(f"{value} {from_unit} = {result} {to_unit}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

        again = input("Do you want to make another conversion? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()
