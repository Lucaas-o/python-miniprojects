import random

# List of words
word_list = [
    "apple", "banana", "orange", "grape", "mango", "lemon", "cherry", "pineapple", "strawberry", "blueberry",
    "peach", "watermelon", "pear", "coconut", "raspberry", "avocado", "kiwi", "plum", "fig", "pomegranate",
    "carrot", "potato", "tomato", "onion", "garlic", "cucumber", "lettuce", "spinach", "broccoli", "cauliflower",
    "pepper", "mushroom", "zucchini", "asparagus", "eggplant", "cabbage", "celery", "radish", "beet", "turnip",
    "bread", "butter", "cheese", "milk", "yogurt", "cream", "egg", "meat", "chicken", "beef", "pork",
    "fish", "shrimp", "salmon", "tuna", "crab", "lobster", "squid", "oyster", "scallop", "clam",
    "sugar", "salt", "pepper", "vinegar", "mustard", "ketchup", "honey", "syrup", "chocolate", "candy",
    "cookie", "cake", "pie", "donut", "brownie", "pudding", "ice cream", "jelly", "jam", "peanut butter",
    "coffee", "tea", "juice", "soda", "water", "lemonade", "smoothie", "beer", "wine", "whiskey",
    "plate", "bowl", "cup", "glass", "fork", "knife", "spoon", "napkin", "table", "chair",
    "window", "door", "wall", "floor", "ceiling", "roof", "chimney", "stairs", "basement", "attic",
    "bed", "pillow", "blanket", "mattress", "closet", "wardrobe", "mirror", "shower", "bathtub", "sink",
    "computer", "phone", "laptop", "tablet", "keyboard", "mouse", "printer", "monitor", "camera", "television",
    "car", "bicycle", "bus", "train", "airplane", "boat", "truck", "motorcycle", "scooter", "subway",
    "road", "highway", "street", "bridge", "tunnel", "traffic", "sign", "light", "crosswalk", "sidewalk",
    "house", "apartment", "building", "hotel", "restaurant", "store", "mall", "market", "factory", "office",
    "book", "magazine", "newspaper", "letter", "envelope", "stamp", "pen", "pencil", "marker", "eraser",
    "school", "student", "teacher", "classroom", "desk", "blackboard", "homework", "test", "exam", "lesson",
    "music", "song", "melody", "rhythm", "lyrics", "guitar", "piano", "violin", "trumpet", "drum",
    "art", "painting", "sculpture", "museum", "gallery", "theater", "film", "actor", "director", "script",
    "science", "biology", "chemistry", "physics", "laboratory", "experiment", "microscope", "telescope", "planet", "star",
    "sun", "moon", "sky", "cloud", "rain", "thunder", "lightning", "storm", "rainbow", "snow",
    "fire", "smoke", "ash", "heat", "cold", "wind", "tornado", "hurricane", "earthquake", "tsunami",
    "animal", "dog", "cat", "bird", "fish", "horse", "cow", "sheep", "goat", "pig",
    "lion", "tiger", "elephant", "monkey", "bear", "wolf", "fox", "rabbit", "squirrel", "kangaroo",
    "insect", "butterfly", "bee", "ant", "spider", "beetle", "mosquito", "dragonfly", "grasshopper", "caterpillar",
    "color", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black",
    "white", "gray", "silver", "gold", "bronze", "copper", "navy", "teal", "cyan", "magenta",
    "body", "head", "face", "eye", "nose", "mouth", "ear", "hand", "arm", "leg",
    "foot", "finger", "toe", "stomach", "heart", "brain", "muscle", "bone", "skin", "hair",
    "clothing", "shirt", "pants", "dress", "skirt", "jacket", "coat", "sweater", "hat", "gloves",
    "shoes", "socks", "scarf", "belt", "tie", "underwear", "swimsuit", "pajamas", "uniform", "apron",
    "time", "day", "night", "morning", "evening", "hour", "minute", "second", "week", "month",
    "year", "calendar", "clock", "season", "spring", "summer", "autumn", "winter", "holiday", "vacation",
    "family", "mother", "father", "brother", "sister", "uncle", "aunt", "cousin", "nephew", "niece",
    "friend", "neighbor", "classmate", "teammate", "boss", "worker", "employee", "customer", "guest", "host",
    "feeling", "happy", "sad", "angry", "excited", "scared", "nervous", "surprised", "bored", "tired",
    "idea", "thought", "dream", "memory", "wish", "plan", "goal", "challenge", "problem", "solution"
]


# Hangman stages representation
HANGMAN_PICS = [
    """
      ------
      |    |
      |    
      |    
      |    
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    =========
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    =========
    """
]

def choose_word():
    """Selects a random word from the word list."""
    return random.choice(word_list).lower()

def initialize_display(word):
    """Creates a hidden word representation (_ _ _)."""
    return ["_" if letter.isalpha() else letter for letter in word]

def update_display_word(word, display_word, guess):
    """Reveals the guessed letter in the display word."""
    return [guess if word[i] == guess else display_word[i] for i in range(len(word))]

def get_valid_guess(guessed_letters):
    """Gets a valid single-letter guess from the user."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def play_hangman():
    """Main game function to play Hangman."""
    word = choose_word()
    display_word = initialize_display(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while wrong_guesses < max_attempts and "_" in display_word:
        print(HANGMAN_PICS[wrong_guesses])  # Show hangman stage
        print("Word: ", " ".join(display_word))
        print("Guessed letters: ", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            display_word = update_display_word(word, display_word, guess)
            print("Correct!")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_attempts - wrong_guesses} attempts left.")

    # Final result
    print(HANGMAN_PICS[wrong_guesses])  # Show final hangman state
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

    print("Game over!")

# Run the game
if __name__ == "__main__":
    play_hangman()
