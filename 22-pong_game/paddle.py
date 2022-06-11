from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)