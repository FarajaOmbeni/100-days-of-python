from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open('day20_21_snakegame/data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(x=0, y=260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('day20_21_snakegame/data.txt', mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over.", False, ALIGNMENT, font=FONT)