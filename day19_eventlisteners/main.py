from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def c_clock():
    tim.setheading(tim.heading()+10)
def clock():
    tim.setheading(tim.heading()-10)
def clear():
    tim.reset()
    

screen.listen()
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="a", fun=c_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick() 