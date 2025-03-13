import time

# Ask the user for the countdown duration in seconds
t = input("When do you want the countdown to end? (Enter time in seconds): ")

def countdown(t):
    """
    Starts a countdown from the given time (in seconds) to 0.
    Args:
        t (int): The total time in seconds for the countdown.
    """
    while t:  # Continue the loop as long as t is greater than 0
        # Calculate minutes and seconds from the total time
        mins, secs = divmod(t, 60)  # divmod divides t by 60 and returns (minutes, seconds)

        # Format the time as MM:SS
        timer = f"{mins:02d}:{secs:02d}"  # :02d ensures two digits for minutes and seconds

        # Print the current time (overwrite the previous line)
        print(timer, end="\r")

        # Update interval of 1s
        time.sleep(1)

        #Decrease the timer by 1s
        t -= 1

    # Print once countdown ends
    print("Time's up!")

countdown(int(t))