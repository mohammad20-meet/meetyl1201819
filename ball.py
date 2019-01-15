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
		if 15>self.radius>10:
			self.dx = 2
			self.dy = 2
		elif 20>self.radius>16:
			self.dx = 1.8
			self.dy = 1.8
		elif 25>self.radius>21:
			self.dx = 1.6
			self.dy = 1.6
		elif 30>self.radius>26:
			self.dx = 1.4
			self.dy = 1.4
		elif 35>self.radius>31:
			self.dx = 1.2
			self.dy = 1.2
		elif 40>self.radius>36:
			self.dx = 1
			self.dy = 1
		elif 45>self.radius>41:
			self.dx = 0.8
			self.dy = 0.8
		elif 50>self.radius>46:
			self.dx = 0.6
			self.dy = 0.6
		elif 55>self.radius>51:
			self.dx = 0.4
			self.dy = 0.4
		elif 60>self.radius>56:
			self.dx = 0.2
			self.dy = 0.2
		elif 65>self.radius>61:
			self.dx = 0.1
			self.dy = 0.1
		elif 70>self.radius>66:
			self.dx = 0.09
			self.dy = 0.09
			
	def grow(self, radius):
		self.radius += radius
		self.shapesize(self.radius/10)
		if self.radius > TOO_BIG:
			self.shapesize(TOO_BIG/10)
			self.radius = TOO_BIG

	def thxforplaying(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
		color = (random.random(),random.random(),random.random())
		self.goto(x,y)
		self.color(color)
		self.shapesize(radius/10)
		self.radius = radius

