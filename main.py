import turtle
# import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# # Score
# score_a = 0
# score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350)

# Ball
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350)

# Function
y_a = paddle_a.ycor()
x_a = paddle_a

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)


def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)


def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

# Main game loop
while True:
    wn.update()