# ----------------------- Debuging -----------------------
# # Describe Problem

'''The error in the below code is in for loop. the range function goes 1-20 but not include 20 so to solve thi we simply put 21 instead of 20 '''
# def my_function():
#   for i in range(1, 20): 
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug
from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
'''The error in the below code is in line 2 the year must be <= 1994'''
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
'''The error in the below code is in prnt statement there's missing f-string'''
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
'''The error in the below code is in line 4, there must be single '=' sign'''
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
'''The error in the below code is in line 5, b_list.append(new_item) must be indented within the for loop'''
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# ---------------------------------------------------------------------------------------------------

# Debugging challenge 1

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# elif num % 2 == 1:
#     print("Number is odd")
# else:
#     print("Please enter a whole number")

