# print("Welcome to Roller Coaster")
# height = int(input("Enter height in cm: "))
# bill = 0
# if height > 120:
#     age = int(input("Enter age: "))
#     if age <= 18:
#         bill = 7
#         print("Pay 7$ for ticket")
#     elif age < 12:
#         bill = 5
#         print("Pay 5$ for ticket")
#     else:
#         bill = 12
#         print("Pay 12$ for ticket")
    
#     pic = input("Do you want to take a picture for only 3$?(Y/N): ")
#     if pic == 'Y':
#         bill +=3

#     print(f"You total bill is {bill}$")
# elif height <= 0:
#     print("Please enter a valid height")
# else:
#     print("You can't ride")  
# -------------------------------------------------------------------------

# Exercise 3.1
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Number is even!")
# elif num % 2 == 1:
#     print("Number is odd!")
# else:
#     print("Invalid Number!")
# -------------------------------------------------------------------------

# Exercise 3.2
# height = float(input("Enter height in meters: "))
# weight = int(input("Enter weight in kg: "))

# BMI = weight / height ** 2
# BMI_RESULT = round(BMI, 1)

# if BMI_RESULT < 18.5:
#     print(f"You BMI is {BMI_RESULT}, you are underweight")

# elif BMI_RESULT >= 18.5 and BMI_RESULT < 25:
#     print(f"You BMI result is {BMI_RESULT}, You have normal weight")

# elif BMI_RESULT >= 25 and BMI_RESULT < 30:
#     print(f"Your BMI result is {BMI_RESULT}, You are overweight")

# elif BMI_RESULT >= 30 and BMI_RESULT < 35:
#     print(f"Your BMI result is {BMI_RESULT}, You are obese")

# elif BMI_RESULT > 35:
#     print(f"Your BMI result is {BMI_RESULT}, You are clinically obese")

# else:
#     print("Error!")
# -------------------------------------------------------------------------

# Challenge 3.3
# year = int(input("Enter a year: "))

# if year % 4 == 0 or year % 400 == 0:
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is not a leap year")
# -------------------------------------------------------------------------

# Challenge 3.4

# print("welcome to Python Pizza Deliveries")

# print("Price list is give bellow")
# print("Small Pizza: 15$")
# print("Medium Pizza: 20$")
# print("Large Pizza: 25$")
# print("Pepperoni for small Pizza: 3$")
# print("Pepperoni for Medium and Large Pizza: 5$")
# print("Extra cheese for any pizza: 1$")

# size = input("What size pizza do you want? (M/S/L) ")
# add_pepperoni = input("Do you want pepperoni to your pizza? (Y/N) ")
# add_cheese = input("Do you want to add cheese to your pizza? (Y/N) ")

# bill = 0

# if size == 'M':
#     bill = 20
#     if add_pepperoni == 'Y':
#         bill += 5
#     if add_cheese == 'Y':
#         bill += 1
#     print(f"Your total bill is {bill}$")

# elif size == 'S':
#     bill = 15
#     if add_pepperoni == 'Y':
#         bill += 3
#     if add_cheese == 'Y':
#         bill += 1
#     print(f"Your total bill is {bill}$")

# elif size == 'L':
#     bill = 25
#     if add_pepperoni == 'Y':
#         bill += 5
#     if add_cheese == 'Y':
#         bill += 1
#     print(f"Your total bill is {bill}$")

# else:
#     print("Have a good day!")
# -------------------------------------------------------------------------

# Challenge 3.5

# your_name = input("Enter your name: ")
# their_name = input("Enter their name: ")

# combined_name = your_name + their_name

# lowercase_name = combined_name.lower()

# t = lowercase_name.count('t')
# r = lowercase_name.count('r')
# u = lowercase_name.count('u')
# e = lowercase_name.count('e')

# true = t + r + u + e

# l = lowercase_name.count('l')
# o = lowercase_name.count('o')
# v = lowercase_name.count('v')
# e = lowercase_name.count('e')

# love = l + o + v + e

# love_score = int(str(true) + str(love))
# print(love_score)

# if love_score < 10 or love_score > 90:
#     print(f"Your love score is {love_score}, you go together like a coke and mentos")
# elif love_score > 40 and love_score < 50:
#     print(f"your love score is {love_score}, you are alright together")
# else:
#      print(f"Your love score is {love_score}")