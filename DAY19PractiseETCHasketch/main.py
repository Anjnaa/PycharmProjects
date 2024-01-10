from turtle import Turtle, Screen

kallu = Turtle()
drishya = Screen()


def move_forward():
    kallu.forward(10)


def move_backward():
    kallu.backward(10)


def move_left():
    new_dir = kallu.heading() + 10
    kallu.setheading(new_dir)


def move_right():
    new_dir = kallu.heading() - 10
    kallu.setheading(new_dir)


def clear():
    kallu.clear()
    kallu.penup()
    kallu.home()
    kallu.pendown()


drishya.listen()
drishya.onkey(move_forward, "f")
drishya.onkey(move_backward, "b")
drishya.onkey(move_left, "l")
drishya.onkey(move_right, "r")
drishya.onkey(clear, "c")

drishya.exitonclick()
