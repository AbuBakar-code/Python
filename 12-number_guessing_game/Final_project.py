import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_dificulty():
    choice = input("Choose a level, Type 'easy' or 'hard': ")
    if choice == 'easy':
        return EASY_LEVEL
    elif choice == 'hard':
        return HARD_LEVEL
    else:
        print("Invalid input!")

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns -1
    elif guess < answer:
        print("Too low!")
        return turns -1
    else:
        print(f"You've got a right answer {answer}")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of number between 1-100")
    answer = random.randint(1, 100)
    turns = set_dificulty()
    guess = 0
    while guess != answer:
        print(f"You've {turns} turns left.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of attempts, You lose. The answer is {answer}")
        elif guess != answer:
            print("Guess agin")
game()
