import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()


def play_game():
    # WELCOME SCREEN
    print("Welcome to Snowman Meltdown!")
    # INITIALIZE GAME
    secret_word = get_random_word()
    print(
        "Secret word selected: " + secret_word)  # for testing, later remove this line
    mistakes = 0
    guessed_letters = []
    # GAME LOOP
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        user_guess = input("Guess a letter: ").lower()
        print("You guessed:", user_guess) # for testing, later remove this line
        if user_guess in secret_word:
            guessed_letters.append(user_guess)
        else:
            mistakes += 1
        # END GAME?
        if mistakes > 2:
            print(f"\nGame over! The word was {secret_word}")
            print(STAGES[3])
            break
        elif set(guessed_letters) == set(secret_word):
            print("\nCongratulations, you saved the snowman!")
            break
