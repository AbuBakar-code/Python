import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
not_false = True
while not_false:
  word = input("Enter a word: ").upper()
  try:
    code = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print('Sorry, only letters in the alphabet please')
  else:
    print(code)
    not_false = False