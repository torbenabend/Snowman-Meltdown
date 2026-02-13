"""
Snowman Meltdown - A simple command-line word guessing game.

The player guesses letters of a randomly chosen word.
Each wrong guess advances the snowman meltdown stage.
The game ends when the word is guessed or too many mistakes are made.
"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Print the current snowman stage and the word progress.

    Args:
    mistakes (int): Number of incorrect guesses.
    secret_word (str): The word to guess.
    guessed_letters (list[str]): Correctly guessed letters.
    """
    print(STAGES[mistakes])
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()


def get_user_guess():
    """
    Prompt the user for a single alphabetical letter.

    Returns:
        str: A validated lowercase letter.
    """
    while True:
        user_guess = input("Guess a letter: ").lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            return user_guess
        print(
            "Invalid input! Please enter a single alphabetical character.\n"
        )


def wants_to_play_again():
    """
    Ask the user whether to start a new game.

    Returns:
        bool: True, if user chooses to play again, False otherwise.
    """
    while True:
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid input! Please enter 'y' for yes and 'n' for no.\n")


def play_game():
    """
    Run the main game loop.

    Initializes the game state, processes guesses,
    and ends when the player wins or exceeds
    the allowed number of mistakes.
    """
    # WELCOME SCREEN
    print("Welcome to Snowman Meltdown!")
    is_game_running = True
    while is_game_running:
        # INITIALIZE GAME
        secret_word = get_random_word()
        print(
            "Secret word selected: " + secret_word)  # for testing, later remove this line
        mistakes = 0
        max_nr_mistakes = len(STAGES) - 1
        guessed_letters = []
        # GAME LOOP
        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            user_guess = get_user_guess()
            print("You guessed:", user_guess) # for testing, later remove this line
            if user_guess in secret_word:
                guessed_letters.append(user_guess)
            else:
                mistakes += 1
            # CHECK WIN AND LOSS CONDITIONS
            if mistakes == max_nr_mistakes:
                print(f"\nGame over! The word was {secret_word}")
                print(STAGES[-1])
                is_game_running = wants_to_play_again()
                break
            if set(guessed_letters) == set(secret_word):
                print("\nCongratulations, you saved the snowman!")
                is_game_running = wants_to_play_again()
                break
    print("Ok, see you next time. Goodbye!")
