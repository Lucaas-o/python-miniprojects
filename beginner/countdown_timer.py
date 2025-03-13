import time
import os
import keyboard  # pip install keyboard

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system("cls" if os.name == "nt" else "clear")

def display_countdown(total_seconds, paused):
    """Display the countdown timer and keybind instructions."""
    clear_screen()
    mins, secs = divmod(total_seconds, 60)
    print("=" * 30)
    print("⏳ Countdown Timer".center(30))
    print("=" * 30)
    print(f"\nTime Remaining: {mins:02d}:{secs:02d}")
    if paused:
        print("\n⏸️  Paused. Press SPACE to Resume.")
    print("\nOptions:")
    print("  SPACE - Pause/Resume")
    print("  S     - Stop")
    print("  R     - Restart")
    print("=" * 30)

def countdown_timer(minutes, seconds):
    """Countdown timer with real-time keybind detection."""
    total_seconds = minutes * 60 + seconds
    paused = False
    
    while total_seconds > 0:
        display_countdown(total_seconds, paused)

        for _ in range(10):
            if keyboard.is_pressed("space"):
                paused = not paused
                time.sleep(0.5)
                break

            if keyboard.is_pressed("s"):
                clear_screen()
                print("\n🛑 Timer stopped!")
                return

            if keyboard.is_pressed("r"):
                clear_screen()
                confirm = input("\n🔄 Restart Timer? (y/n): ").strip().lower()
                if confirm == "y":
                    print("\n🔄 Restarting...")
                    time.sleep(1)
                    main()
                    return
                else:
                    print("\n❌ Restart cancelled.")
                    time.sleep(1)
                    break

            if not paused:
                time.sleep(0.1)
            else:
                time.sleep(0.1)

        if not paused:
            total_seconds -= 1

    clear_screen()
    print("\n⏲️ Time's up! 🎉")
    if os.name == "nt":
        os.system("echo \a")

def main():
    """Main function to get user input and start countdown."""
    clear_screen()
    print("⏲️ Countdown Timer (Press SPACE to Pause/Resume, S to Stop, R to Restart)")
    
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        if minutes < 0 or seconds < 0 or seconds >= 60:
            print("⚠️ Please enter valid time values!")
            return

        countdown_timer(minutes, seconds)

    except ValueError:
        print("⚠️ Invalid input! Please enter numbers.")

if __name__ == "__main__":
    main()
