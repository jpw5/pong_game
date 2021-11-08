from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'e')
screen.onkey(l_paddle.go_down, 's')


def start_game():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            time.sleep(0.1)

        # Detect R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        if scoreboard.l_score == 5 or scoreboard.r_score == 5:
            scoreboard.game_over()
            game_is_on = False


screen.onkey(start_game, 'g')
screen.exitonclick()
