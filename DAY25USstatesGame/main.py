"""US STATES GAME"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Desktop/Downloads/50_states.csv")
# # print(data)
all_states = data.state.to_list()
# # print(all_states)
guessed_state = []
#


while len(guessed_state) < 50:
    answered_state = screen.textinput(title="Guess the State", prompt="What is next State in you mind?").title()
    # print(answered_state)
    if answered_state =="Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(new_data)
    if answered_state in all_states:
        guessed_state.append((answered_state))
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answered_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
#

screen.exitonclick()




# def click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(click)
# turtle.mainloop()
