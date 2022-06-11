# Day 5 Final Project
import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters= int(input("How many letters would you like in your password? ")) 
num_of_symbols = int(input("How many symbols would you like? "))
num_of_digits = int(input("How many digits would you like? "))
# ------------------------------------------
# Easy level
# password =""
# for char in range(1, num_of_letters + 1):
#     random_char = random.choice(letters)
#     password +=random_char

# num = ""
# for i in range(1, num_of_digits + 1):
#     random_num = random.choice(numbers)
#     num += random_num

# sym = ""
# for i in range(1, num_of_symbols + 1):
#     random_sym = random.choice(symbols)
#     sym += random_sym

# final_password = password + num + sym 
# print(final_password)
# ------------------------------------------
# Hard level
password = []
for char in range(1, num_of_letters + 1):
    random_char = random.choice(letters)
    password +=random_char

for i in range(1, num_of_digits + 1):
    random_num = random.choice(numbers)
    password += random_num

for i in range(1, num_of_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

print(password)
pas = ""
for i in password:
    pasw = random.choice(password)
    pas += pasw


print(f"You Password is: {pas}")