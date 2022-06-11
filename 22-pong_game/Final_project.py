from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score_board = Score_board()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detection with paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.bounce_x()
    
    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score_board.l_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        score_board.r_point()

screen.exitonclick()