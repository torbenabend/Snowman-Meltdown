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
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)


def get_display_word(secret_word, guessed_letters):
    """
    Create a formatted string showing the current guessing progress.

    Reveals correctly guessed letters and replaces
    remaining letters with underscores.

    Args:
        secret_word (str): The word to guess.
        guessed_letters (set[str]): Letters guessed so far.

    Returns:
        str: The formatted word with spaces between characters.
    """
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    return display_word


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Print the current snowman stage and the word progress.

    Args:
    mistakes (int): Number of incorrect guesses.
    secret_word (str): The word to guess.
    guessed_letters (set[str]): Correctly guessed letters.
    """
    print(STAGES[mistakes])
    print("Word: ", get_display_word(secret_word, guessed_letters))
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


def has_lost(mistakes, max_mistakes):
    """
    Check whether the player has lost the game.

    Args:
        mistakes (int): Number of incorrect guesses made.
        max_mistakes (int): Maximum allowed incorrect guesses.

    Returns:
        bool: True if the player reached the maximum mistakes, False otherwise.
    """
    return mistakes == max_mistakes


def has_won(secret_word, guessed_letters):
    """
    Check whether the player has won the game.

    Args:
        secret_word (str): The word to guess.
        guessed_letters (set[str]): Letters guessed so far.

    Returns:
        bool: True if all letters in the secret word have been guessed, False otherwise.
    """
    return guessed_letters == set(secret_word)


def play_single_game():
    """
    Run a single game session of Snowman Meltdown.

    Initializes the secret word, mistake counter, and guessed letters.
    Loops until the player wins or loses, updating the game state
    and displaying the snowman and guessed letters.
    """
    # INITIALIZE GAME
    secret_word = get_random_word()
    mistakes = 0

    guessed_letters = set()
    # GAME LOOP
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        user_guess = get_user_guess()
        if user_guess in secret_word:
            guessed_letters.add(user_guess)
        else:
            mistakes += 1
        # CHECK WIN AND LOSS CONDITIONS
        if has_lost(mistakes, MAX_MISTAKES):
            print(f"\nGame over! The word was {secret_word}")
            print(STAGES[-1])
            break
        if has_won(secret_word, guessed_letters):
            print("\nCongratulations, you saved the snowman!")
            break


def play_game():
    """
    Run the full Snowman Meltdown game session.

    Greets the player, starts single game sessions, and
    prompts after each game whether the player wants to
    continue. Ends when the player chooses not to play again.
    """
    # WELCOME SCREEN
    print("Welcome to Snowman Meltdown!")
    # START GAME
    while True:
        play_single_game()
        if not wants_to_play_again():
            break
    # END GAME
    print("Ok, see you next time. Goodbye!")
