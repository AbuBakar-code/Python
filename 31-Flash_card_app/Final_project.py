from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
current_card = {}
try:
  data = pandas.read_csv('learn_words.csv')
except FileNotFoundError:
  orignal_data = pandas.read_csv('french_words.csv')
  data_dict = orignal_data.to_dict(orient='records')
else:
  data_dict = data.to_dict(orient='records')

def new_card():
  global current_card, flip_timmer
  window.after_cancel(flip_timmer)
  current_card = random.choice(data_dict)
  canvas.itemconfig(card_title, text='French', fill='black')
  canvas.itemconfig(card_word, text=current_card["French"], fill='black')
  canvas.itemconfig(card_background, image= card_front_img)
  flip_timmer = window.after(3000, func=flip_card)

def flip_card():
  canvas.itemconfig(card_title, text='English', fill="white")
  canvas.itemconfig(card_word, text=current_card['English'], fill="white")
  canvas.itemconfig(card_background, image= card_back_img)

def is_known():
  data_dict.remove(current_card)
  data = pandas.DataFrame(data_dict)
  data.to_csv('learn_words.csv', index=False)
  new_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timmer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file='card_back.png')
card_front_img = PhotoImage(file='card_front.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file='wrong.png')
cross_button = Button(image= cross_img, highlightthickness=0, command= new_card)
cross_button.grid(column=0, row=1)

tick_img = PhotoImage(file='right.png')
tick_button = Button(image= tick_img, highlightthickness=0, command= is_known)
tick_button.grid(column=1, row=1)

new_card()

window.mainloop()