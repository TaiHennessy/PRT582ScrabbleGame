import time
import random
import threading
import nltk
from nltk.corpus import words

# Ensure the NLTK words corpus is downloaded
nltk.download('words')

# Load the word list from NLTK
WORD_LIST = set(words.words())

LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Function to calculate Scrabble score
def scrabble_score(word):
    word = word.upper()
    if not word.isalpha():
        raise ValueError("Word must only contain alphabetic characters.")
    return sum(LETTER_VALUES[char] for char in word)

# Function to get the required word length
def get_word_length():
    return random.randint(3, 7)

# Function to validate the word length
def validate_word(word, required_length):
    if len(word) != required_length:
        raise ValueError(f"Word must be {required_length} characters long.")
    return word

# Function to check if the word is valid using NLTK dictionary
def is_valid_word(word):
    return word.lower() in WORD_LIST

# Function to display a countdown timer
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\rTime left: {timer}\n", end="")
        time.sleep(1)
        print("\033[F", end="")  # Move cursor up to keep input on the second line
        seconds -= 1
    print("\rTime left: 00:00\n", end="")

# Main game loop
def game_loop():
    total_score = 0
    rounds = 10
    while rounds > 0:
        required_length = get_word_length()
        print(f"\nPlease enter a word of length {required_length}: ")
        
        # Start timer in a separate thread
        timer_thread = threading.Thread(target=countdown_timer, args=(15,))
        timer_thread.start()
        
        # Capture user input
        start_time = time.time()
        word = input("\n")  # Ensure the input appears on a separate line
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        if elapsed_time > 15:
            print("Time's up! You took too long.")
            continue
        
        try:
            # Validate word length
            word = validate_word(word, required_length)
            
            # Validate dictionary word
            if not is_valid_word(word):
                print("Not a valid word. Please try again.")
                continue
            
            # Calculate score
            score = scrabble_score(word)
            # Bonus points for quicker entries
            bonus = max(0, 15 - elapsed_time)
            total_score += score + bonus
            
            print(f"Word score: {score}, Time bonus: {bonus:.2f}, Total score: {total_score:.2f}")
        
        except ValueError as e:
            print(e)
            continue
        
        rounds -= 1
        if input("Continue (y/n)? ").lower() != 'y':
            break
    
    print(f"Final score: {total_score:.2f}")

if __name__ == "__main__":
    game_loop()