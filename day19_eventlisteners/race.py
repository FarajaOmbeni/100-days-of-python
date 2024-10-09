from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a bet", prompt="Which turtle will wil the race? Enter color")

colors = ["red", 'orange', 'yellow', 'green', 'blue', 'purple']
start_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()