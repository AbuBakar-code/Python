# import random

# random_int = random.randint(1, 10)
# print(random_int)
# -------------------------------------------------------------------------
# Exercise 4.1
# random_num = random.randint(0,1)
# if random_num == 0:
#     print("Tails")
# elif random_num == 1:
#     print("Heads")
# else:
#     print("Invalid entry!")
# -------------------------------------------------------------------------
# Exercise 4.2
# logic 1
# name_string = input("Enter persons name seperated by commas: ")
# names = name_string.split(',')
# length = len(names)

# random_choice = random.randint(0, length - 1)
# person = names[random_choice]
# print(f"{person} has to pay for meal")
# -------------------------------------------------------------------------
# logic 2
# person_names =  input("Enter persons name seperated by commas: ")
# names = person_names.split(',')
# person = random.choice(names)
# print(person + " has to pay for meal")
# -------------------------------------------------------------------------

# Exercise 4.3
# row1 = ["#", "#", "#"]
# row2 = ["#", "#", "#"]
# row3 = ["#", "#", "#"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put your treasure? ")

# horizontal = int(position[0])
# verticle = int(position[1])

# selected_row = map[verticle - 1]
# selected_row[horizontal - 1] = "*"

# print(f"{row1}\n{row2}\n{row3}")

# -------------------------------------------------------------------------


