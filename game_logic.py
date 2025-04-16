import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state: snowman and guessed word."""
    print("\n" + STAGES[mistakes] + "\n")
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("\nRemaining mistakes:", MAX_MISTAKES - mistakes)
    print("Guessed letters:", ", ".join(sorted(list(guessed_letters))))
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    word_length = len(secret_word)
    correctly_guessed_count = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES and correctly_guessed_count < word_length:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
            correctly_guessed_count = 0
            for letter in secret_word:
                if letter in guessed_letters:
                    correctly_guessed_count += 1
        else:
            mistakes += 1
            print("Incorrect guess.")

    display_game_state(mistakes, secret_word, guessed_letters)

    if correctly_guessed_count == word_length:
        print("Congratulations, you saved the snowman! The word was:", secret_word)
    else:
        print("Game Over! The snowman melted. The word was:", secret_word)

if __name__ == "__main__":
    play_game()

