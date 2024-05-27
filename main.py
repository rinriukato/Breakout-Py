from turtle import Screen
from paddle import Paddle
from ball import Ball
from block_manager import BlockManager
from scoreboard import Scoreboard
# TODO: Create Powerups Class
from time import sleep

# Game Consts
PLAYER_START_POS = -350
GAME_SPEED = 0.01
WIDTH = 600
HEIGHT = 800
X_BOUNDARY = 280
Y_BOUNDARY = 390
PADDLE_COLI_DIST = 22


# Initialize Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("Breakout!")
screen.tracer(0)

# Initialize Paddles
player = Paddle()
player.set_position(0, PLAYER_START_POS)

# Initialize Ball
ball = Ball()
ball.setposition(player.xcor(), player.ycor() + 15)

# Initialize Scoreboard
scoreboard = Scoreboard()

block_manager = BlockManager(scoreboard)
block_manager.create_blocks()

# Key-Input Event Listeners
screen.listen()
screen.onkey(fun=player.move_left, key='Left')
screen.onkey(fun=player.move_right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(GAME_SPEED)
    ball.move()

    # Check if ball is touching any walls
    if ball.xcor() > X_BOUNDARY or ball.xcor() < - X_BOUNDARY:
        ball.bounce_x_dir()

    if ball.ycor() > Y_BOUNDARY:
        ball.bounce_y_dir()

    # Check for paddle collision
    if ball.distance(player) < PADDLE_COLI_DIST:
        if ball.can_ball_bounce_off_paddle():
            ball.bounce_y_dir()

    if block_manager.check_collision(ball):
        if ball.can_ball_bounce_off_block():
            ball.bounce_y_dir()

    # Check if player is out of bounds, therefore game over
    if ball.ycor() < -Y_BOUNDARY:
        game_is_on = False

screen.exitonclick()