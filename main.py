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
    if GameBall.xcor() >= 380 or GameBall.xcor() <= -380:
        game_is_on = False

    if GameBall.ycor() >= 300 or GameBall.ycor() <= -300:
        GameBall.collision("y")

    if GameBall.xcor() >= 340 and GameBall.distance(RightPaddle) < 50:
        GameBall.collision("x")

    if GameBall.xcor() <= -340 and GameBall.distance(LeftPaddle) < 50:
        GameBall.collision("x")

    sleep(0.1)

GameScreen.exitonclick()
