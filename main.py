import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tur = Player()
car_manager=CarManager()
level=Scoreboard()
screen.listen()
screen.onkey(tur.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    ##Detecting Collision when hit with a car:
    for car in car_manager.all_cars:
        if tur.distance(car) < 20:
            level.game_over()
            game_is_on = False
    ##Detecting When turtle reached top:
    if tur.ycor() > FINISH_LINE_Y:
        tur.return_position()
        car_manager.increase_speed()
        level.level_up ()

screen.exitonclick()
