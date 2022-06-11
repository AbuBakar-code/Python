# Turtle race game and bet on turtles
from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? ")
is_race_on = False

turtle_color = ['red', 'blue', 'purple', 'orange', 'green']
turtle_pos = [70, 40, 10, -20, -50]
all_turtles = []
for t_pos in range (0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle_color[t_pos])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=turtle_pos[t_pos])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You won!, {winning_color} is the winner")
            else:
                print(f"You lost!, {winning_color} is the winner")
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)













screen.exitonclick()