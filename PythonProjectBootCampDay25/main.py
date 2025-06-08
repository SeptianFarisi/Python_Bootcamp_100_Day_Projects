from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S Guess State")
screen.setup(800, height=600)
screen.addshape("blank_states_img.gif")
turtle = Turtle()
turtle.shape("blank_states_img.gif")
data = pd.read_csv("50_states.csv")
len_data = len(data.state)
list_states = data.state.to_list()
guess_data = pd.read_csv("miss_state.csv")
mising_states = []
mising_states.append(guess_data)
print(list_states)

while len(mising_states) < 50:
    answer = screen.textinput(f"{len(mising_states)}/{len_data} state correct","What's another state's name?").title()
    if answer == "Exit":
        break
    if answer == "Save":
        miss_states = pd.DataFrame(mising_states)
        miss_states.to_csv("miss_state.csv")
    if answer in list_states:
        mising_states.append(answer)
        new_data = data[data["state"] == answer]
        t = Turtle()
        t.hideturtle()
        t.penup()
        new_x = int(new_data.x.iloc[0])
        new_y = int(new_data.y.iloc[0])
        t.goto(new_x, new_y)
        t.write(arg=answer, font=("monaco", 6, "bold"))

