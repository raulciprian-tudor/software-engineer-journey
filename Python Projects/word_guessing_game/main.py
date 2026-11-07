import random


def main():
    """Main"""
    start_game()


def start_game():
    """Start the game"""
    life = 6
    game_round = 0

    secret = secret_word()
    hidden_secret = hide_secret(secret)

    while life >= 0:
        print(f"{hidden_secret=}")
        guess = input("Guess: ")

        if game_round == 0:
            print(f"Secret word: {hidden_secret}")

        if check_if_in_word(guess, secret):
            hidden_secret = update_secret(hidden_secret, secret, guess)
            print(f"Word: {hidden_secret}")
        else:
            life -= 1

        if life == 0:
            print("You lost!")
            print(f"The secret word was: {secret}")

        if guess == "exit":
            print("Exiting game...")
            break


def check_if_in_word(letter, secret):
    """Check if the guessed letter exists in the secret word"""
    if letter in secret:
        return True


def update_secret(hidden_secret, secret, letter):
    """If letter guessed exists in letter, update the secret to show the letter"""
    # chars = list(hidden_secret)
    # for char in secret:
    #     if char == letter:
    #         chars[secret.index(char)] = letter
    # updated_secret = "".join(chars)
    # return updated_secret
    for i, ch in enumerate(secret):
        print(i, ch)
    return "demo"


def secret_word():
    """Random secret word picker"""
    words = ["car", "house", "airplane", "building", "helicopter"]
    return random.choice(words)


def hide_secret(secret):
    """Hide the secret word by replacing all letters with _"""

    secret_length = len(secret) - 1
    hidden_secret = ""

    while secret_length >= 0:
        hidden_secret += "_"
        secret_length -= 1

    return hidden_secret


main()
