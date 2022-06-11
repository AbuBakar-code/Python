# def greet(name):
#     print(f"Hello {name}, Have a nice day!")

# greet("Abubakar")

# -------------------------------------------------------------------------

# def greet(name, loc):
#     print(f"Hello {name}, The event location is {loc}")

# greet(name = "Abubakar", loc = "FoodStreet phase 6 Hayatabad, Peshawar")

# -------------------------------------------------------------------------

# Challenge 1 cans of paint 
# import math
# test_h = int(input("Enter height of a wall: "))
# test_w = int(input("Enter width of a wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     cans = (height * width) / cover
#     number_of_cans = math.ceil(cans)
#     print(f"You will need {number_of_cans} cans of paint to paint the wall")

# paint_calc(height= test_h, width= test_w, cover= coverage)

# -------------------------------------------------------------------------

# Challenge 2 Prime number checker

# n = int(input("Enter a number: "))

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is a prime number")
#     else:
#         print("It is not a prime number!")

# prime_checker(number=n)

