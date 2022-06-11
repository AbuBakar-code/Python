from art import logo
import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10 , 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You loose"
    elif user_score == 0:
        return "You wins"
    elif user_score > 21:
        return "You loose"
    elif computer_score > 21:
        return "You wins"
    elif computer_score < user_score:
            return "You Win"
    else:
            return "You loose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # Deals user cards
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards are: {user_cards}, user score is: {user_score}")
        print(f"computer's first cards is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        
        user_choice = input("Type 'y' to add a card, type 'n' to paas.  ").lower()
        if user_choice == 'y':
            user_cards.append(deal_cards())
        else:
            is_game_over = True
        
    # Deals computer cards
    while computer_score != 0 and computer_score <= 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" You final cards are {user_cards} and you score is {user_score}")
    print(f" computer final cards are {computer_cards} and computer score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game? (Y/N) ").upper() == "Y":
    print(logo)
    play_game()
