import random
from stages import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    word_to_show = "_" * len(secret_word)
    print("Word: ", end="")
    for c in secret_word:
        if c in guessed_letters:
            print(f"{c} ", end="")
        else:
            print("_ ", end="")
    print()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    mistakes = 0
    guessed_letters = set()
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = "1"
        while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
            guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        guessed_letters.add(guess[0].lower())
        if guess not in secret_word:
            mistakes += 1
        if mistakes > 3:
            break


if __name__ == "__main__":
    play_game()