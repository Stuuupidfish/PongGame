import turtle

wn = turtle.Screen()
wn.title("hamsterball")
wn.bgcolor("DarkSeaGreen2")
wn.setup(width=800, height=600)
wn.tracer(0)
# This function is used to turn turtle animation on or off and set a delay for update drawings.

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
# speed for animation not paddle
paddle_a.shape("square")
paddle_a.color("turquoise4")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# we don't want to draw line while moving
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("turquoise4")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("turquoise4")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.12
ball.dy = -0.12
# d=delta

pen = turtle.Turtle()
pen.speed(0)
pen.color("turquoise4")
pen.penup()
pen.hideturtle()
# we only wanna see the text
pen.goto(0,250)
pen.write("ham: 0  ster: 0", align="center", font=("Comic Sans MS", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
# tells it to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("ham: {}  ster: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("ham: {}  ster: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

# keeps the window continuously up
