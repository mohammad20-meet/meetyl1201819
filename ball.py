from turtle import *
import random
import math
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
TOO_BIG = 150

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy

	def move(self,SCREEN_WIDTH,SCREEN_HEIGHT):
		oldx = self.xcor()
		oldy = self.ycor()		
		newx = oldx + self.dx
		newy = oldy + self.dy
		right_side_ball = (newx + self.radius)
		left_side_ball = (newx - self.radius)
		top_side_ball = (newy + self.radius)
		bottom_side_ball = (newy - self.radius)
		self.goto(newx,newy)
		if top_side_ball > SCREEN_HEIGHT:
			self.dy = -self.dy
		if bottom_side_ball < -SCREEN_HEIGHT:
			self.dy = -self.dy

		if right_side_ball > SCREEN_WIDTH:
			self.dx = -self.dx
		if left_side_ball < -SCREEN_WIDTH:
			self.dx = -self.dx

	def speed(self):
		if self.radius <=16:
			self.dx = -9 if self.dx < 0 else 9
			self.dy = -9 if self.dy <0 else 9
		elif 20>=self.radius and self.radius>=16:
			self.dx = -8.5 if self.dx < 0 else 8.5
			self.dy = -8 if self.dy <0 else 8
		elif 25>=self.radius and self.radius>=21:
			self.dx = -8 if self.dx < 0 else 8
			self.dy = -8 if self.dy <0 else 8
		elif 30>=self.radius and self.radius>=26:
			self.dx = -7.5 if self.dx < 0 else 7.5
			self.dy = -7.5 if self.dy <0 else 7.5
		elif 35>=self.radius and self.radius>=31:
			self.dx = -7 if self.dx < 0 else 7
			self.dy = -7 if self.dy <0 else 7
		elif 40>=self.radius and self.radius>=36:
			self.dx = -6.5 if self.dx < 0 else 6.5
			self.dy = -6.5 if self.dy <0 else 6.5
		elif 45>=self.radius and self.radius>=41:
			self.dx = -6 if self.dx < 0 else 6
			self.dy = -6 if self.dy <0 else 6
		elif 50>=self.radius and self.radius>=46:
			self.dx = -5.5 if self.dx < 0 else 5.5
			self.dy = -5.5 if self.dy <0 else 5.5
		elif 55>=self.radius and self.radius>=51:
			self.dx = -5 if self.dx < 0 else 5
			self.dy = -5 if self.dy <0 else 5
		elif 60>=self.radius and self.radius>=56:
			self.dx = -4.5 if self.dx < 0 else 4.5
			self.dy = -4.5 if self.dy <0 else 4.5
		elif 65>=self.radius and self.radius>=61:
			self.dx = -4 if self.dx < 0 else 4
			self.dy = -4 if self.dy <0 else 4
		elif 70>=self.radius and self.radius>=66:
			self.dx = -3.5 if self.dx < 0 else 3.5
			self.dy = -3.5 if self.dy <0 else 3.5
			
	def grow(self, radius):#Function to make the ball Grow
		self.radius += radius
		self.shapesize(self.radius/10)
		if self.radius > TOO_BIG:
			self.shapesize(TOO_BIG/10)
			self.radius = TOO_BIG

	def thxforplaying(self, SCREEN_WIDTH, SCREEN_HEIGHT):#Function to make the Ball Teleport after Death
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
		color = (random.random(),random.random(),random.random())
		self.goto(x,y)
		self.color(color)
		self.shapesize(radius/10)
		self.radius = radius

