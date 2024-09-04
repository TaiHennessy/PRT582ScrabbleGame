import time 
import random
import nltk
from nltk.corpus import words

"""

Calculate the Scrabble score for a given word.
Args:
    word (str): The word to calculate the score for.
Returns:
    int: The total score of the word.
Raises:
    ValueError: If the word contains non-alphabetic characters.
"""


# Ensure the NLTK (Natural Language Toolkit library) words corpus is downloaded 
nltk.download('words')

# Load the word list from NLTK 
WORD_LIST = set(words.words())


# Dictionary of letter values for Scrabble
LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Calculate Scrabble score
def scrabble_score(word):
    word = word.upper() # Requirment 2 - Case insensitive
    if not word.isalpha():
        raise ValueError("Word must only contain alphabetic characters.") # Requirment 3 - Only alphabetic characters
    return sum(LETTER_VALUES[char] for char in word) # Requirment 1 - Calculate the score

# Get the required word length
def get_word_length():
    return random.randint(3, 7)

# Validate the word length
def validate_word(word, required_length):
    if len(word) != required_length:
        raise ValueError(f"Word must be {required_length} characters long.")
    return word

# Requirment 5 - check if the word is valid using NLTK dictionary
def is_valid_word(word):
    return word.lower() in WORD_LIST

# Main loop
def game_loop():
    total_score = 0
    rounds = 10 # Requirment 6 - 10 rounds
    while rounds > 0:
        required_length = get_word_length()
        print(f"Please enter a word of length {required_length}: ")
        
        # Start timer
        start_time = time.time()
        
        # User input
        word = input()
        
        # Requirment 4  - Calculate elapsed time 
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
        if input("Continue (y/n)? ").lower() != 'y': # Requirment 6 - User can quit
            break
    
    print(f"Final score: {total_score:.2f}")

if __name__ == "__main__": # Run the game loop
    game_loop()
