from turtle import *
import random
import math
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 70
MINIMUM_BALL_DX = 5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

NUMBER_OF_DEATH = 5
MINIUM_DEATH_RADIUS = 10
MAXIMUM_DEATH_RADIUS = 70
MINIMUM_DEATH_DX = 5
MAXIMUM_DEATH_DX = 5
MINIMUM_DEATH_DY = -5
MAXIMUM_DEATH_DY = 5
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
	def move(self,width,height):
		oldx = self.xcor()
		oldy = self.ycor()		
		newx = oldx + self.dx
		newy = oldy + self.dy
		right_side_ball = (newx + self.radius)
		left_side_ball = (newx - self.radius)
		top_side_ball = (newy + self.radius)
		bottom_side_ball = (newy - self.radius)
		self.goto(newx,newy)
		if right_side_ball>width:
			self.dx = -self.dx

		if left_side_ball<-width:
			self.dx = -self.dx

		if top_side_ball>height:
			self.dy = -self.dy

		if bottom_side_ball<-height:
			self.dy = -self.dy
	def speed(self):
		if 15>ball.radius>10:

		elif 20>ball.radius>16:

		elif 25>ball.radius>21:

		elif 30>ball.radius>26:

		elif 35>ball.radius>31:

		elif 40>ball.radius>36:

		elif 45>ball.radius>41:

		elif 50>ball.radius>46:

		elif 55>ball.radius>51:

		elif 60>ball.radius>56:

		elif 65>ball.radius>61:

		elif 70>ball.radius>66:
			
	def grow(self, radius):
		self.radius += radius
		self.shapesize(self.radius/10)
		if self.radius > MAXIMUM_BALL_RADIUS:
			self.shapesize(MAXIMUM_BALL_RADIUS/10)

	def thxforplaying(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
		color = (random.random(),random.random(),random.random())
		self.goto(x,y)
		self.color(color)
		self.shapesize(radius/10)
		self.radius = radius


