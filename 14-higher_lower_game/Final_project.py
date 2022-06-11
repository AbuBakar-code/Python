import random
from art import logo, vs
from data import data

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
choice = True
account_b = random.choice(data)

while choice:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Guess a right option (A/B): ")

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    isCorrect = check_answer(guess, a_follower_count, b_follower_count)

    if isCorrect:
        score += 1
        print(f"You're right, Your current score is {score}")
    else:
        choice = False
        print(f"You are wrong, Your score is {score}")