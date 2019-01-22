import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(1, 2, 3, 4, 20, "yellow", "circle")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []

x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS

for i in range(NUMBER_OF_BALLS):
	pass
		   