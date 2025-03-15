import os
import random
import time

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print("\n   0   1   2")
    for i, row in enumerate(board):
        colored_row = []
        for cell in row:
            if cell == "X":
                colored_row.append(f"{RED}X{RESET}")
            elif cell == "O":
                colored_row.append(f"{BLUE}O{RESET}")
            else:
                colored_row.append(" ")
        print(f"{i}  {' | '.join(colored_row)}")
        if i < 2:
            print("  " + "-" * 13)
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def simple_ai_move(board):
    empty_cells = get_empty_cells(board)
    for player in ["O", "X"]:
        for row, col in empty_cells:
            board[row][col] = player
            if check_winner(board, player):
                board[row][col] = " "
                return row, col
            board[row][col] = " "
    return random.choice(empty_cells) if empty_cells else None

def play_game():
    scores = {"X": 0, "O": 0, "Draws": 0}
    
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        turn = 0
        mode = input("Select mode (1: PvP, 2: PvAI): ").strip()
        ai_mode = mode == "2"
        
        while True:
            print_board(board)
            print(f"Scores - X: {scores['X']} | O: {scores['O']} | Draws: {scores['Draws']}")
            player = players[turn % 2]
            
            if ai_mode and player == "O":
                print("AI is thinking...")
                time.sleep(1)
                move = simple_ai_move(board)
                if move:
                    row, col = move
                else:
                    break
            else:
                try:
                    move = input(f"Player {player}, enter row and column (0-2, space-separated) or 'q' to quit: ").strip()
                    if move.lower() == 'q':
                        return
                    row, col = map(int, move.split())
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        print("Numbers must be between 0 and 2!")
                        time.sleep(1.5)
                        continue
                except ValueError:
                    print("Invalid input! Use format: 'row col' (e.g., '1 1')")
                    time.sleep(1.5)
                    continue

            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                time.sleep(1.5)
                continue

            board[row][col] = player
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                scores[player] += 1
                time.sleep(2)
                break
            
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                scores["Draws"] += 1
                time.sleep(2)
                break
            
            turn += 1
        
        replay = input("Play again? (y/n): ").lower().strip()
        if replay != "y":
            print("\nFinal Scores:")
            print(f"X: {scores['X']} | O: {scores['O']} | Draws: {scores['Draws']}")
            break

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("X is Red, O is Blue")
    play_game()
    print("Thanks for playing!")