from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x=0,y=240)
        self.hideturtle()
        self.draw_line()
    
    def draw_line(self):
        gaps = [270, 200, 130, 60, -10, -80, -150, -220, -290, -300]
        for i in gaps:
            self.goto(x=0, y=i)
            self.write("|", False, align="center",  font=('Courier', 40, 'normal'))