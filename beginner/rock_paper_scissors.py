import random
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def bot_turn():
    """Randomly selects Rock, Paper, or Scissors for the bot."""
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    return choices[random.randint(1, 3)]

def player_turn(player_select):
    """Converts the player's selection to Rock, Paper, or Scissors."""
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    return choices.get(player_select, "Invalid selection")

def determine_winner(player_choice, bot_choice):
    """Determines the winner of the game."""
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and bot_choice == "Scissor") or \
         (player_choice == "Scissor" and bot_choice == "Paper") or \
         (player_choice == "Paper" and bot_choice == "Rock"):
        return "You win!"
    else:
        return "Bot wins!"

def main():
    clear_screen()
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        print("4. Exit")

        try:
            player_select = int(input("Enter your choice (1-4): "))
            if player_select == 4:
                print("Thanks for playing! Goodbye!")
                break

            player_choice = player_turn(player_select)
            if player_choice == "Invalid selection":
                print("Invalid choice. Please select 1, 2, or 3.")
                continue

            bot_choice = bot_turn()
            print(f"\nYou chose: {player_choice}")
            print(f"Bot chose: {bot_choice}")

            result = determine_winner(player_choice, bot_choice)
            print(result)

            input("\nPress Enter to continue...")
            clear_screen()

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")
            clear_screen()

if __name__ == "__main__":
    main()