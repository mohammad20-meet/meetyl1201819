import turtle
import time
import random
from ball import *
turtle.tracer(0, 0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

My_BALL =  Ball(10,-30,-50,30,30,"green")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 70
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

turtle.bgcolor("pink")
BALLS = []

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


def collide(ball_a,ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D+10<ball_a.radius+ball_b.radius:
		return True
	else:
		return False
def check_myball_collision(self):																																																																														
		if collide(My_BALL,ball_a,ball_b):
			if My_BALL.radius>ball_a.radius or ball_b.radius:
				My_BALL.grow(ball_a.radius) or My_BALL.grow(ball_b)
				ball_a or ball_b.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
			if ball_a or Ball_b > My_BALL.radius:
				ball_a or ball_b.grow(My_BALL.radius)
				My_BALL.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)


def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):
				if ball_a.radius> ball_b.radius:
					ball_a.grow(ball_b.radius)
					ball_b.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				elif ball_b.radius>ball_a.radius:
					ball_b.grow(ball_a.radius)
					ball_a.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)


while RUNNING:
	move_all_balls()
	time.sleep(SLEEP)
	check_all_balls_collision()
	turtle.update()