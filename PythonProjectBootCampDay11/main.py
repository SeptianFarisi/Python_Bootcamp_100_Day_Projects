import random
from art import logo


def calculate_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, Computer has blackjack"
    elif p_score == 0:
        return "You win, You has blackjack"
    elif p_score > 21:
        return "You lose"
    elif c_score > 21:
        return "You win"
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose"

def game():
    print(logo)
    player_card = []
    computer_card = []
    player_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        player_card.append(random_card())
        computer_card.append(random_card())

    while not is_game_over:
        player_score = calculate_card(player_card)
        computer_score = calculate_card(computer_card)
        print(f"Your card {player_card}, current score {player_score}")
        print(f"Computer first card {computer_card[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_hit = input("type 'y' to hit card, type 'n' to pass? ").lower()
            if player_hit == "y":
                player_card.append(random_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(random_card())
        computer_score = calculate_card(computer_card)

    print(f"Player hands {player_card}, final score {player_score}")
    print(f"Computer hands {computer_card}, final score {computer_score}")
    print(compare(player_score, computer_score))

while input("You want play blackjack? type 'y' or 'n'\n").lower() == "y":
    game()