from turtle import Turtle

class Player(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)
    
    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)