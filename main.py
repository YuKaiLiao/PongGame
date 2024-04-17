from time import sleep
from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball

GameScreen = Screen()
GameScreen.setup(800, 600)
GameScreen.bgcolor("black")
GameScreen.title("Pong")
GameScreen.tracer(0)

RightPaddle = Paddle((350, 0), ("Up", "Down"))
LeftPaddle = Paddle((-350, 0), ("w", "s"))

GameBall = Ball()

game_is_on = True
while game_is_on:
    GameScreen.update()
    GameBall.move()
    sleep(0.1)

GameScreen.exitonclick()
