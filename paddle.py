from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.speed(0)
        self.goto(xpos, ypos)
        # self.setheading(90)
        own_screen = self.screen
        own_screen.listen()
        own_screen.onkey(self.go_up, "Up")
        own_screen.onkey(self.go_down, "Down")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
