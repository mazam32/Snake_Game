from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakes.up,"Up")
screen.onkey(snakes.down,"Down")
screen.onkey(snakes.left,"Left")
screen.onkey(snakes.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snakes.move()

    if snakes.head.distance(food) < 15:
        food.new_positon()
        scoreboard.increase_score()
        snakes.extend()

    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        scoreboard.reset()
        snakes.reset()

    for turtles in snakes.all_turtles[1:]:
        if (snakes.head.distance(turtles) < 10):
            scoreboard.reset()
            snakes.reset()

screen.exitonclick()