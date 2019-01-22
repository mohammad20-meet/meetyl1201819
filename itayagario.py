import turtle
import time
import random
from itayball import Ball
import math

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(1, 2, 3, 4, 20, "yellow")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []

x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		i.speed()

for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		i.speed()
	
def collide(ball_a, ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D<ball_a.r+ball_b.r:
		return True
	else:
		return False 

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):
				rad_a = ball_a.r
				rad_b = ball_b.r
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = (random.random(),random.random(),random.random())
				if rad_a > rad_b:
					if ball_a.r < MAXIMUM_BALL_RADIUS:
						ball_a.r += 1
						ball_a.shapesize(ball_a.r/10)
						ball_b.x = x
						ball_b.y = y
						ball_b.dx = dx
						ball_b.dy = dy
						ball_b.r = r
						ball_b.color( color)
						ball_b.goto(x, y)
						ball_b.shapesize(ball_b.r/10)
				else:
					if ball_b.r < MAXIMUM_BALL_RADIUS:
						ball_b.r += 1
						ball_b.shapesize(ball_a.r/10)
						ball_a.x = x
						ball_a.y = y
						ball_a.dx = dx
						ball_a.dy = dy
						ball_a.r = r
						ball_a.color( color)
						ball_a.goto(x, y)
						ball_a.shapesize(ball_b.r/10)
				
def check_myball_collision():
	for ball_c in BALLS:
		if collide(MY_BALL, ball_c):
			if MY_BALL.r > ball_c.r:
				if MY_BALL.r < MAXIMUM_BALL_RADIUS:
					MY_BALL.r += 1
					MY_BALL.shapesize(ball_a.r/10)
					ball_c.x = x
					ball_c.y = y
					ball_c.dx = dx
					ball_c.dy = dy
					ball_c.r = r
					ball_c.color( color)
					ball_c.goto(x, y)
					ball_c.shapesize(ball_b.r/10)
			else:
					return False

	return True

def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y  

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING is True:
	move_all_balls()
	check_myball_collision()
	check_all_balls_collision()
	turtle.update()
	

		   