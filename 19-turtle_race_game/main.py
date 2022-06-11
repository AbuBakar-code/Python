# Event Listeners and make turtle to move and draw shapes using keyboard stokes

from turtle import Turtle, Screen, setheading


t = Turtle()
screen = Screen()

t.pensize(3)

def move_fd():
    t.fd(10)

def move_backward():
    t.backward(10)

def clock():
    newHeading = t.heading() + 10
    t.setheading(newHeading)

def anti_clock():
    newHeading = t.heading() - 10
    t.setheading(newHeading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.speed('fastest')

screen.listen()
screen.onkey(key= "w", fun= move_fd)
screen.onkey(key= "s", fun= move_backward)
screen.onkey(key= "a", fun= anti_clock)
screen.onkey(key= "d", fun= clock)
screen.onkey(key= "c", fun= clear)
screen.exitonclick()