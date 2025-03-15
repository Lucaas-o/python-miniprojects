# clear_screen.py
import os

def clear_screen():
    """
    Clears the terminal screen. Works on Windows ('cls') and Unix-based systems ('clear').
    """
    if os.name == 'nt':  # Windows
        _ = os.system('cls')
    else:  # Unix-based (Linux, macOS)
        _ = os.system('clear')