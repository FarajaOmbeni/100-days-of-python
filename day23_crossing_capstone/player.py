from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish = FINISH_LINE_Y
        self.color('black')
        self.shape('turtle')
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def restart_game(self):
        self.goto(STARTING_POSITION)
    
