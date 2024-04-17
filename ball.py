from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.speed(0)

    def move(self):
        current_position = self.position
        new_position_x = self.xcor() + 10
        new_position_y = self.ycor() + 10
        new_position = (new_position_x, new_position_y)

        self.goto(new_position)
