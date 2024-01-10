# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.color("#C71585")
#
# for value in range(4):
#     for _ in range(4):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.left(90)
#
#
# screen = Screen()
# screen.exitonclick()



# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
#            "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = int(360 / num_sides)
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shapes in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shapes)
#
# screen = Screen()
# screen.exitonclick()



#
# import turtle as t
# from turtle import Screen
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colours = (r, g, b)
#     return colours
#
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
# #            "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()



import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()