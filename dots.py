from turtle import Turtle
import random
TOO_BIG1 = 150
NUMBER_OF_Dots = 120
MINIMUM_Dot_RADIUS = 5
MAXIMUM_Dot_RADIUS = 5
class Dot(Turtle):
	def __init__(self,x,y,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
	def grow(self, radius):
		self.radius += radius
		self.shapesize(self.radius/10)
		if self.radius > TOO_BIG1:
			self.shapesize(TOO_BIG1/10)
		self.radius = TOO_BIG1

	def thxforplaying(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_Dot_RADIUS , SCREEN_WIDTH - MAXIMUM_Dot_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_Dot_RADIUS , SCREEN_HEIGHT - MAXIMUM_Dot_RADIUS)
		color = (random.random(),random.random(),random.random())
		self.goto(x,y)
		self.color(color)
