# try:
#   file = open('file.txt')
#   dictionary = {'key': 'value'}
#   print(dictionary['key'])
# except FileNotFoundError:
#   file = open('file.txt', 'w')
#   file.write('abubakar')
# except KeyError as error_message:
#   print(f'The key {error_message} does not found')
# else:
#   content = file.read()
#   print(content)
# finally:
#   file.close()
#   print('File was closed')

# height = float(input("Enter height in metres: "))
# weight = int(input("Enter weight in kilo grams: "))

# if height > 3:
#   raise ValueError("Human height cannot be over 3 meters!")

# bmi = weight / height ** 2
# print(bmi)
# --------------------------------------------------------------

# Exercise 30.1

# fruits = ['Apple', 'Pear', 'Mango', 'Banana']

# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("Fruit Pie")
#   else:
#     print(fruit + ' Pie')

# make_pie(1)
# --------------------------------------------------------------

# Exercise 30.2

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#   try:
#     total_likes = total_likes + post['Likes']
#   except KeyError:
#     pass


# print(total_likes)

# --------------------------------------------------------------

# Exercise 30.3

# import pandas as pd

# df = pd.read_csv('nato_phonetic_alphabet.csv')

# phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# not_false = True
# while not_false:
#   word = input("Enter a word: ").upper()
#   try:
#     code = [phonetic_dict[letter] for letter in word]
#   except KeyError:
#     print('Sorry, only letters in the alphabet please')
#   else:
#     print(code)
#     not_false = False