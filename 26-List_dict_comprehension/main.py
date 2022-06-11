
# List comprehension

# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)
# ---------------------------------------------

# name = 'Abubakar'
# new_list = [letter for letter in name]
# print(new_list)
# ---------------------------------------------

# new_list = [num + num for num in range(1,5)]
# print(new_list)
# ---------------------------------------------

# names = ['abubakar', 'kamran', 'ali', 'umar']
# new_names = [name.upper() for name in names if len(name) > 5 ]
# print(new_names)
# ---------------------------------------------

# Exersice 26.1
# numbers = [1, 1, 2, 3, 5, 8, 10]
# sqrd_numbers = [num*num for num in numbers]
# print(sqrd_numbers)

# ---------------------------------------------

# Exercise 26.2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 32, 43, 13]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# Exercise 26.3
# with open('file1.txt') as file1:
#     file1_data = file1.readlines()

# with open('file2.txt') as file2:
#     file2_data = file2.readlines()

# new_list = [int(num) for num in file1_data if num in file2_data]
# print(new_list)

# ---------------------------------------------------------

# Disctionary Comprehension
# import random

# names = ['abubakar', 'kamran', 'ali', 'umar']
# student_score = {student:random.randint(1,100) for student in names}
# # print(student_score)
# passed_student = {student:score for (student, score) in student_score.items() if score > 50}
# print(passed_student)

# ---------------------------------------------------------

# Exercise 26.4

# string = "This is a string of many words" 
# word_dict = {word : len(word)  for word in string.split() }
# print(word_dict)

# ---------------------------------------------------------

# Exercise 26.5

# temperature = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# temp_in_f = {day: (temp * 9/5) + 32 for (day, temp) in temperature.items()}
# print(temp_in_f)

# Looping dictionaries throug pandas
# import pandas as pd

# data = {
#     "students": ['abubakar', 'huzaifa', 'umer', 'usman'],
#     "score": [80, 60, 78, 98]
# }

# new_data = pd.DataFrame(data)
# for (key, value) in data.items():
#      print(value)

# looping dict thorugh each data frames

# for (index, row) in new_data.iterrows():
#     print(row)