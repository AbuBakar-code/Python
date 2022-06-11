# Day 3 final project
from art import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right_choice = input("You are at the cross road. Where you wanna go? (L/R): ")
if left_right_choice == 'R':
    print("Game Over!")
elif left_right_choice == 'L':
    swim_or_wait = input("Do you wanna swim or wait? (S/W): ")
    if swim_or_wait == 'S':
        print("Game Over!")
    elif swim_or_wait == 'W':
        which_door = input("Which door you wanna go? (R/B/Y): ")
        if which_door == 'Y':
            print("You win!")
        else:
            print("Game over!")