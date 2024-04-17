from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, control_key):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.speed(0)
        self.goto(pos[0], pos[1])
        # self.setheading(90)
        own_screen = self.screen
        own_screen.listen()
        own_screen.onkey(self.go_up, control_key[0])
        own_screen.onkey(self.go_down, control_key[1])

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
