# Day 9 final project

from art import logo

print(logo)

bid_dict = {}
choice  = True

def highest_bid_record(bid_record):
    highest_bid = 0
    winner_name = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder
    print(f"The winner is {winner_name} with a bid of ${bid_amount}")
    


while choice:
    name = input("Enter your name: ")
    bid = int(input("Enter a bid amount: $"))

    bid_dict[name] = bid
    user_choice = input("Do you want to enter another name? (Y/N)").upper()
    if user_choice == 'N':
        choice = False
        highest_bid_record(bid_dict)