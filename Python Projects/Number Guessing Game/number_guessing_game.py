import random


def main():
    start_game()


def start_game():
    cards_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    user_score = 0
    game_round = 0
    card_1 = 0
    user_lost = False

    print("Game started!")

    while user_lost is False:
        if game_round == 0:
            card_1 = pick_card(cards_deck)
            cards_deck.remove(card_1)
            print(f"Card 1: {card_1}")

        user_guess = input("Higher or Lower? ").lower()

        card_2 = pick_card(cards_deck)
        cards_deck.remove(card_2)

        if (
            card_1 > card_2
            and user_guess == "higher"
            or card_1 < card_2
            and user_guess == "lower"
        ):
            print(f"card1: {card_1} | card2: {card_2}")
            print("You lost.")
            print(f"Score: {user_score}")
            user_lost = True
        elif (
            card_1 < card_2
            and user_guess == "higher"
            or card_1 > card_2
            and user_guess == "lower"
        ):
            print(f"card1: {card_1} | card2: {card_2}")
            print("You won!")
            user_score += 1
            card_1 = card_2
            game_round += 1

        if user_guess == "exit":
            print("Stopping game..")
            user_lost = True

        if len(cards_deck) == 0:
            cards_deck = reset_deck(card_1)


def pick_card(deck):
    return random.choice(deck)


def reset_deck(current_card):
    cards_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    cards_deck.remove(current_card)
    return cards_deck


main()
