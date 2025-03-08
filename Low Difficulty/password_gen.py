import random

# Define a list of typical password-allowed characters
valid_characters = (
    [chr(i) for i in range(97, 123)]  # Lowercase letters (a-z)
    + [chr(i) for i in range(65, 91)]  # Uppercase letters (A-Z)
    + [str(i) for i in range(0, 10)]  # Digits (0-9)
    + ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']  # Common special characters
)

# Validate password length
length = 0
while length < 8 or length > 100:
    print("Your password length must be at least 8 and less than 100.")
    try:
        length = int(input("How long you want the password to be (in characters): "))
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
password = ''.join(random.choice(valid_characters) for _ in range(length))
print(f"Your secure password is: {password}")