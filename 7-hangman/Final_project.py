# Day 7 final project
import random
from hangman_words import word_list
from hangman_art import stages, logo 

print(logo)
print("Guess a word")
random_word = random.choice(word_list)
print(random_word)

word = []

for letter in random_word:
    word += '_'
print(word)
lives =  6
end_of_game = False
while not end_of_game:

    user_input = input("Enter an alphabet: ").lower()
    if user_input in word:
      print("You entered a same letter")
    for i in range(len(random_word)):
        letter = random_word[i]
        if user_input == letter:
            word[i] = letter
    if user_input not in random_word:
       lives -= 1
       print(f"The letter {user_input} is not in the word. Your remaining lives are {lives}")
       if lives == 0:
          end_of_game = True
          print("You Loose")
          print(f"The word is {random_word}")

    print(word)
    if '_' not in word:
        end_of_game = True
        print("You win")

    print(stages[lives])

# Another logic:
# a = '_'
# while a in word:
#     user_input = input("Enter an alphabet: ").lower()

#     for i in range(len(random_word)):
#         letter = random_word[i]
#         if user_input == letter:
#             word[i] = letter

#     print(word)

# print("You win")
