from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [120, 80, 40, 0, -40, -80, -120]
all_tattu = []

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the Race? Enter color of that "
                                                          "Turtle: ")
for position in range(7):
    tim = Turtle(shape="turtle")
    tim.color(colors[position])
    tim.penup()
    tim.goto(x=-230, y=y_positions[position])
    all_tattu.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for tattu in all_tattu:
        if tattu.xcor() > 230:
            is_race_on = False
            winning_color = tattu.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} tattu is the winner.")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 11)
        tattu.forward(rand_distance)

screen.exitonclick()
