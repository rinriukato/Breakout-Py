from turtle import Turtle

MOVE_SPEED = 20
X_BOUNDS = 255


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=0.5)

    def set_position(self, x_cord: int, y_cord: int):
        self.setposition(x_cord, y_cord)

    def move_right(self):
        if self.xcor() <= X_BOUNDS:
            new_x = self.xcor() + MOVE_SPEED
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() >= -X_BOUNDS:
            new_x = self.xcor() - MOVE_SPEED
            self.goto(new_x, self.ycor())
