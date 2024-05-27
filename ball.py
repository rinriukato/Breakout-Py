from turtle import Turtle
from random import random
from timeit import default_timer as timer

DEFAULT_SPEED = 5
PADDLE_COOLDOWN = 1 # in seconds
BLOCK_COOLDOWN = 0.03

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_dir = 1
        self.y_dir = 1
        self.speed = DEFAULT_SPEED
        self.latest_paddle_timestamp = timer()
        self.latest_block_timestamp = timer()

    def set_position(self, x_cord: int, y_cord: int):
        self.setposition(x_cord, y_cord)

    def move(self):
        new_x = self.xcor() + (self.speed * self.x_dir)
        new_y = self.ycor() + (self.speed * self.y_dir)
        self.goto(new_x, new_y)

    def bounce_y_dir(self):
        self.y_dir *= -1

    def bounce_y_dir_random(self):
        self.y_dir = 1
        self.y_dir *= -1 * random()
        print(f'New Y Dir - {self.y_dir}')

    def bounce_x_dir(self):
        self.x_dir *= -1

    def bounce_x_dir_random(self):
        self.x_dir = 1
        self.x_dir *= -1 * random()

    def set_paddle_last_hit_timestamp(self):
        self.latest_paddle_timestamp = timer()

    def set_block_last_hit_timestamp(self):
        self.latest_block_timestamp = timer()

    def can_ball_bounce_off_paddle(self) -> bool:
        end = timer()
        elapsed_time = end - self.latest_paddle_timestamp
        print(f'Paddle Elapsed: {elapsed_time}')

        # If it has more than one second since this ball bounced off a paddle, you are allowed to bounce
        if elapsed_time > PADDLE_COOLDOWN:
            self.set_paddle_last_hit_timestamp()
            return True
        # Otherwise, ball cannot bounce off of this paddle again.
        else:
            return False

    def can_ball_bounce_off_block(self) -> bool:
        end = timer()
        elapsed_time = end - self.latest_block_timestamp
        print(f'Block Elapsed: {elapsed_time}')

        # If it has more than one second since this ball bounced off a block, you are allowed to bounce
        if elapsed_time > BLOCK_COOLDOWN:
            self.set_block_last_hit_timestamp()
            return True
        # Otherwise, ball cannot bounce off of this block again.
        else:
            return False
