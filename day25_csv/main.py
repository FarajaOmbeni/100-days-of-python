import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

states = df.state.to_list()

guessed_states = []

def write_to_screen(state, x, y):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)
    tim.pendown()
    tim.write(state)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct", prompt="What's another state's name?").title()

    if answer_state == 'exit'.title():
        missing_states = [state for state in states if state not in guessed_states]
        final_missed = pd.DataFrame({
            'Missed States': missing_states
            })
        final_missed.to_csv('missed_states.csv')
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        x = df[df.state == answer_state].x.item()
        y = df[df.state == answer_state].y.item()
        write_to_screen(answer_state, x, y)