# Day 8 Final Project caeser cipher encoder decoder
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Logic 1
def encrypt(txt, shft):
    cipher_text = ""
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position + shft
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded word is {cipher_text}")

def decrypt(cipher_text, shft):
    txt = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shft
        new_letter = alphabet[new_position]
        txt += new_letter
    print(f"The decoded word is {txt}")


# Optimised logic
def caeser(choice, txt, shft):
    end_text = ""
    if choice == 'decode':
        shft *= -1
    for char in txt:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shft
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {choice}d result is: {end_text} ")

go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt: ")
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the number of shift: "))
    shift = shift % 26
    caeser(choice=direction, txt=text, shft=shift)

    result = input("Type yes if you wanna go again, Otherwise Type no: ")
    if result == 'no':
        go_again = False
        print("GoodBye!")

if direction == 'encode':
    encrypt(txt=text, shft=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shft=shift)
else:
    print("Error!")
