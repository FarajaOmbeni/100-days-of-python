from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x=0,y=240)
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"{self.lscore} {self.rscore}", False, align="center",  font=('Courier', 40, 'normal'))