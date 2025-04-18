'''
Concepts to Focus On:

Reading CSV Data in Python
DataFrames & Series
Working with Rows & Columns
Data Analysis with Pandas

'''

import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")

print(df)

screen = turtle.Screen()
screen.title("Guess the States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

correct_states = []
# states_list = df.state.to_list()

while len(correct_states) < 50:
    user_input = screen.textinput(title=f"{len(correct_states)}/50 States Guessed", prompt="Name a State").title()

    if user_input == "Exit":
        missing_states = []
        for state in df.state.to_list():
            if state not in correct_states:
                missing_states.append(state)
        new_csv = pd.DataFrame(missing_states)
        new_csv.to_csv("states_to_learn.csv")
        break

    
    if user_input in df.state.to_list():
        if user_input not in correct_states:
            correct_states.append(user_input)
            check_input = df[df.state == user_input]
            print(check_input)
            print(correct_states)
            x_axis, y_axis = int(check_input.x), int(check_input.y)
            t.goto(x_axis, y_axis)
            t.write(f"{user_input}")

