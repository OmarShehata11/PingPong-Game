import turtle
import time
import random

wind = turtle.Screen()
wind.title("ping pong game")
wind.bgcolor("black")
wind.setup(width=800, height=700)
wind.tracer(0)

madrb1 = turtle.Turtle()
madrb1.speed(0)
madrb1.shape("square")
madrb1.color("red")
madrb1.penup()
madrb1.goto(-370, 0)
madrb1.shapesize(stretch_wid=5, stretch_len=1)

madrb2 = turtle.Turtle()
madrb2.speed(0)
madrb2.shape("square")
madrb2.color("blue")
madrb2.penup()
madrb2.shapesize(stretch_len=1, stretch_wid=5)
madrb2.goto(370, 0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.dy = 2
ball.dx = 2

score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 310)
score.hideturtle()

first_win = turtle.Turtle()
first_win.speed(0)
first_win.goto(0, 0)
first_win.hideturtle()
first_win.penup()
first_win.color("red")

second_win = turtle.Turtle()
second_win.speed(0)
second_win.goto(0, 0)
second_win.hideturtle()
second_win.penup()
second_win.color("blue")

intro = turtle.Turtle()
intro.speed(0)
intro.goto(0, 0)
intro.hideturtle()
intro.penup()
intro.color("green")


def madrb1_up():
    y = madrb1.ycor()
    if y < 300:
        y += 20
        madrb1.sety(y)


def madrb1_down():
    y = madrb1.ycor()
    if y > -300:
        y -= 20
        madrb1.sety(y)


def madrb2_up():
    y = madrb2.ycor()
    if y < 300:
        y += 20
        madrb2.sety(y)


def madrb2_down():
    y = madrb2.ycor()
    if y > -300:
        y -= 20
        madrb2.sety(y)


wind.listen()
wind.onkeypress(madrb1_up, "w")
wind.onkeypress(madrb1_down, "s")
wind.onkeypress(madrb2_up, "Up")
wind.onkeypress(madrb2_down, "Down")

k = 5

if __name__ == '__main__':
    while k >= 1:
        intro.clear()
        wind.update()
        intro.write(f"GAME STRATS IN \n       {k}", align="center", font=("courier", 50, "normal"))
        time.sleep(1)
        k -= 1

    while True:
        wind.update()
        score.clear()
        intro.clear()

        score.write(f"first player = {score1}     second player = {score2} ", align="center",
                    font=("courier", 24, "normal"))

        ball.x = random.randint(-100, 100)
        ball.y = random.randint(-100, 100)

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.dy *= -1

        if ball.xcor() > 391:
            ball.goto(ball.x, ball.y)
            score1 += 1

        # when the ball hits the madrab ...--echo-- first time ( my try )..
        """
            if (ball.xcor() > 342) and (ball.xcor() < 352) and (ball.ycor() < madrb2.ycor() + 50) and (ball.ycor() > madrb2.ycor() - 50) or ((ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < madrb1.ycor() + 50 ) and (ball.ycor() > madrb1.ycor() - 50)):
                ball.dx *= -1
            """
        # when the ball hits the madrab ..--echo--.. second time ..
        if (ball.xcor() > 342) and (ball.xcor() < 352) and (ball.ycor() < madrb2.ycor() + 50) and (
                ball.ycor() > madrb2.ycor() - 50):
            ball.dx = ball.dx
            ball.dy = ball.dy
            ball.dx *= -1

        if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < madrb1.ycor() + 50) and (
                ball.ycor() > madrb1.ycor() - 50):
            ball.dx = ball.dx
            ball.dy = ball.dy
            ball.dx *= -1

        if ball.xcor() < -391:
            ball.goto(ball.x, ball.y)
            score2 += 1

        if score1 == 20:
            first_win.write("FIRST PLAYER WON!", align="center", font=("courier", 50, "normal"))
            time.sleep(4)
            break
        elif score2 == 20:
            second_win.write("SECOND PLAYER WON!", align="center", font=("courier", 50, "normal"))
            time.sleep(4)
            break
