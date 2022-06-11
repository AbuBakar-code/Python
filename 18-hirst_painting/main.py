from turtle import Turtle, Screen
import random
import colorgram

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('dark olive green')
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

# t = Turtle()

# Dashed line
# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# Draw diferent shapes
# colors = ['red', 'blue', 'brown', 'gray', 'yellow', 'green', 'pink', 'purple', 'dark olive green', 'olive', 'peach puff']

# def draw_shape(sides):
#     angle = 360 / sides
#     for i in range(sides):
#         t.fd(100)
#         t.right(angle)

# for side in range(3, 11):
#     t.color(random.choice(colors))
#     draw_shape(side)


# Random walk
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randomColor = (r, g, b)
#     return randomColor

# direction = [0, 90, 180, 270]
# t.speed("fastest")
# t.pensize(10)
# for _ in range(500):
#     t.color(random_color())
#     t.fd(30)
#     t.setheading(random.choice(direction))


# Draw Spirograph
# t.pensize(2)
# t.speed("fastest")
# def draw_spirograph(gap):
#     for i in range(int(360/gap)):
#         t.color(random_color())
#         t.setheading(t.heading() + gap)
#         t.circle(100)

# draw_spirograph(10)

# To extract colors from the picture
# rgb_colors = []
# color = colorgram.extract('hirst_painting.webp', 30)
# for clr in color:
#     r = clr.rgb.r
#     g = clr.rgb.g
#     b = clr.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)



# screen = Screen()
# screen.exitonclick()



