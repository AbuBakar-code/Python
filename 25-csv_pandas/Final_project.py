from tkinter import mainloop
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title('US-States Game')

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
is_game_on = True
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 states are correct", prompt="Whats another state name? ").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_state]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('States_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





# below peice of code is to find the coordinates of turtle on screen whereever we click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() 