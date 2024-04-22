from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.speed(0)
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        new_position_x = self.xcor() + self.x_movement
        new_position_y = self.ycor() + self.y_movement
        new_position = (new_position_x, new_position_y)

        self.goto(new_position)

    def collision(self, wall_dir):
        if wall_dir == "y":
            self.y_movement *= -1
        elif wall_dir == "x":
            self.x_movement *= -1
