from turtle import Turtle
from turtle import Screen
from paddle import Paddle

GameScreen = Screen()
GameScreen.setup(800, 600)
GameScreen.bgcolor("black")
GameScreen.title("Pong")
GameScreen.tracer(0)

RightPaddle = Paddle(350, 0)
LeftPaddle = Paddle(-350, 0)

game_is_on = True
while game_is_on:
    GameScreen.update()

GameScreen.exitonclick()
