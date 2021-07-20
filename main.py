from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

score=Scoreboard()


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on=True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.x_bounce()
        score.increase_score()
        score.update_scoreboard

    if ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.x_bounce()
        score.increase_score()
        score.update_scoreboard

    if ball.xcor()>360 or ball.xcor()<-360:
        ball.reset()
        score.game_over()
        game_is_on=False


         
screen.exitonclick()