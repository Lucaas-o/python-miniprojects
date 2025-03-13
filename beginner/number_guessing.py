import random

# Function to get the correct ordinal suffix for a number
def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

# Loop until a valid difficulty is selected
Difficulty = input("Select a difficulty (Easy, Medium, Hard): ")
while Difficulty not in ["Easy", "Medium", "Hard"]:
    Difficulty = input("Select a difficulty (Easy, Medium, Hard): ")

# Generate a random number based on the selected difficulty
if Difficulty == "Easy":
    findMe = random.randint(1, 50)
elif Difficulty == "Medium":
    findMe = random.randint(1, 200)
elif Difficulty == "Hard":
    findMe = random.randint(1, 500)

attempts = 1
test = 0
while test != findMe:
    try:
        test = int(input(f"Enter your {ordinal(attempts)} try: "))
        attempts += 1
        if test > findMe:
            print("Your number is too high.")
        elif test < findMe:
            print("Your number is too small.")
    except ValueError:
        print("Please enter a valid integer.")

print(f"You found {findMe} in {attempts - 1} attempts.")