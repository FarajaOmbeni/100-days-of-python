import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(player.move_up, 'Up')
    screen.onkeypress(player.move_down, 'Down')

    car_manager.create_car()
    car_manager.move_cars()

    #Detect when player hits a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect when player reaches finish line
    if player.ycor() > player.finish:
        scoreboard.score += 1
        scoreboard.update_score()
        player.restart_game()
        car_manager.level_up()

screen.exitonclick()