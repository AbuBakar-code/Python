from turtle import Turtle, Screen, colormode
import random

color_list = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242), (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21), (236, 165, 170), (98, 125, 160), (167, 207, 192), (22, 79, 91), (162, 203, 212)]

t = Turtle()
colormode(255)
t.penup()
t.hideturtle()
t.setheading(220)
t.fd(300)
t.setheading(0)
t.speed("fastest")
num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    t.dot(15, random.choice(color_list))
    t.fd(30)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.fd(30)
        t.setheading(180)
        t.fd(300)
        t.setheading(0)

screen = Screen()
screen.exitonclick()