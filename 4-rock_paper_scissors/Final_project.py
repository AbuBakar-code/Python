# Day 4 final project
import random
from art import rock, paper, scissors

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0: for rock, 1: for paper, 2: for scissors:  "))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)

print("Computer Choice")
print(game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You enter an invalid number!")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")

elif user_choice == 0 and computer_choice == 1:
    print("You Loose")

elif user_choice == computer_choice:
    print("Draw")

elif user_choice == 1 and computer_choice == 0:
    print("You Win!")

elif user_choice == 1 and computer_choice == 2:
    print("You Loose")

elif user_choice == 2 and computer_choice == 0:
    print("You Loose")

elif user_choice == 2 and computer_choice == 1:
    print("You Win!")