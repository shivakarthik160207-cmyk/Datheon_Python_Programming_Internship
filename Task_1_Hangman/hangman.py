import random


HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


# Words for the game
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "database",
    "software",
    "algorithm",
    "function",
    "variable",
    "keyboard"
]


def display_word(word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    secret_word = random.choice(WORDS)

    guessed_letters = set()
    wrong_guesses = set()

    max_wrong_attempts = 6

    print("\n================================")
    print("      HANGMAN WORD GAME")
    print("================================")

    while len(wrong_guesses) < max_wrong_attempts:

        print(HANGMAN_STAGES[len(wrong_guesses)])

        current_display = display_word(secret_word, guessed_letters)

        print("Word:", current_display)

        if wrong_guesses:
            print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
        else:
            print("Wrong guesses: None")

        print("Attempts remaining:",
              max_wrong_attempts - len(wrong_guesses))

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
            continue

        # Correct guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct! 👍")
        else:
            wrong_guesses.add(guess)
            print("Wrong guess! ❌")

        # Check whether the player won
        if all(letter in guessed_letters for letter in secret_word):
            print("\n================================")
            print("       YOU WIN! 🎉")
            print("================================")
            print("The word was:", secret_word)
            print(HANGMAN_STAGES[len(wrong_guesses)])
            return

    # Player lost
    print(HANGMAN_STAGES[max_wrong_attempts])

    print("\n================================")
    print("       GAME OVER! 😢")
    print("================================")
    print("The word was:", secret_word)


if __name__ == "__main__":
    play_game()