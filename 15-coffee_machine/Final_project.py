from coffee_data import MENU, resources

def is_resource_sufficient(ingridiants):
    is_enough = True
    for items in ingridiants:
        if ingridiants[items] > resources[items]:
            print(f"Sorry insufficiant {items}")
            is_enough = False
        return is_enough

def process_coin():
    print("Please insert coins")
    total = int(input("How many Quarters? ")) * .25
    total += int(input("How many Dims? ")) * .10
    total += int(input("How many Nickles? ")) * .05
    total += int(input("How many Pennies? ")) * .01
    return total

def is_transaction_successful(amount_recieved, drink_cost):
    global profit
    if amount_recieved > drink_cost:
        change = round(amount_recieved - drink_cost, 2)
        print(f"Here's your ${change} in change")
        profit += drink_cost
        return True
    else:
        print("Sorry insufficent money")
        return False

def make_coffee(drink, ingridiant):
    for items in ingridiant:
        resources[items] -= ingridiant[items] 
    print(f"Here's your {drink}")

profit = 0
choice = True
while choice:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        choice = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink["ingredients"])
