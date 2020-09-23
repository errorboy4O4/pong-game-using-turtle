# import turtle
#
# nanu = turtle.Screen()
# nanu.title("pong")
# nanu.bgcolor("red")
# nanu.setup(width=800, height=600)
# nanu.tracer(0)
# # PLAYER1
# player1 = turtle.Turtle()
# player1.shape("square")
# player1.color("aqua")
# player1.shapesize(stretch_wid=6, stretch_len=1)
# player1.penup()
# player1.goto(-350, 0)
# # PLAYER2
# player2 = turtle.Turtle()
# player2.shape("square")
# player2.color("green")
# player2.shapesize(stretch_wid=6, stretch_len=1)
# player2.penup()
# player2.goto(350, 0)
#
# # CIRCLE
# circle = turtle.Turtle()
# circle.shape("circle")
# circle.color("gold")
# circle.shapesize(stretch_wid=2, stretch_len=2)
# circle.penup()
# circle.goto(0, 0)
# circle.dx = 0.5
# circle.dy = -0.5
#
#
# def player1_up():
# 	y = player1.ycor()
# 	y += 20
# 	player1.sety(y)
#
#
# def player1_down():
# 	y = player1.ycor()
# 	y -= 20
# 	player1.sety(y)
#
#
# def player2_up():
# 	y = player2.ycor()
# 	y += 20
# 	player2.sety(y)
#
#
# def player2_down():
# 	y = player2.ycor()
# 	y -= 20
# 	player2.sety(y)
#
#
# nanu.listen()
# nanu.onkeypress(player1_up, "w")
# nanu.onkeypress(player1_down, "s")
# nanu.onkeypress(player2_up, "Up")
# nanu.onkeypress(player2_down, "Down")
#
# while True:
# 	nanu.update()
#
# 	circle.setx(circle.xcor() + circle.dx)
# 	circle.sety(circle.ycor() + circle.dy)
#
#
# 	if circle.ycor() > 290:
# 		circle.sety(290)
# 		circle.dy *= -1
#
# 	if circle.ycor() < -290:
# 		circle.sety(-290)
# 		circle.dy *= -1
#
# 	if circle.xcor() > 390:
# 		circle.goto(0, 0)
# 		circle.dx *= -1
#
# 	if circle.xcor() < -390:
# 		circle.goto(0, 0)
# 		circle.dx *= -1
#
# 	if (circle.xcor() > 340 and circle.xcor() < 350) and (circle.ycor() < player2.ycor() + 40 and circle.ycor() > player2.ycor() - 40):
# 		circle.setx(340)
# 		circle.dx *= -1
#
# 	if (circle.xcor() < -340 and circle.xcor() > -350) and (circle.ycor() < player1.ycor() + 40 and circle.ycor() > player1.ycor() - 40):
# 		circle.setx(-340)
# 		circle.dx *= -1

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

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
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
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


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
	wn.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking

	# Top and bottom
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("afplay bounce.wav&")

	elif ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("afplay bounce.wav&")

	# Left and right
	if ball.xcor() > 350:
		score_a += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		ball.goto(0, 0)
		ball.dx *= -1

	elif ball.xcor() < -350:
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		ball.goto(0, 0)
		ball.dx *= -1

	# Paddle and ball collisions
	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.dx *= -1
		os.system("afplay bounce.wav&")

	elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.dx *= -1
		os.system("afplay bounce.wav&")
