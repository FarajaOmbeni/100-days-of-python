from turtle import Screen, Turtle
from players import Player
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_player = Player(x_cor=350, y_cor=0)
l_player = Player(x_cor=-350, y_cor=0)
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkeypress(r_player.move_up, 'Up')
screen.onkeypress(r_player.move_down, 'Down')
screen.onkeypress(l_player.move_up, 'w')
screen.onkeypress(l_player.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    r_collision = ball.distance(r_player) < 50 and ball.xcor() > 320
    l_collision = ball.distance(l_player) < 50 and ball.xcor() < -320
    if r_collision or l_collision:
        ball.bounce_x()
    
    #Detect If right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_round()
        scoreboard.lscore += 1
        scoreboard.update_score()

    #Detect If right paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_round()
        scoreboard.rscore += 1
        scoreboard.update_score()

screen.exitonclick()