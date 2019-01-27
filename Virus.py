import random
from turtle import Turtle

NUMBER_OF_Viruss = 3 
MINIMUM_Virus_RADIUS = 60
MAXIMUM_Virus_RADIUS = 65

class Virus(Turtle):
	def __init__(self,x,y,radius,color):
		Turtle.__init__(self)
		
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
	def grow(self, radius):#Function to make the ball Grow
		self.radius += radius
		self.shapesize(self.radius/10)
		if self.radius > TOO_BIG:
			self.shapesize(TOO_BIG/10)
			self.radius = TOO_BIG

	def thxforplaying(self, SCREEN_WIDTH, SCREEN_HEIGHT):#Function to make the Virus Teleport after Death
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_Virus_RADIUS , SCREEN_WIDTH - MAXIMUM_Virus_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_Virus_RADIUS , SCREEN_HEIGHT - MAXIMUM_Virus_RADIUS)
		radius = random.randint(MINIMUM_Virus_RADIUS,MAXIMUM_Virus_RADIUS)
		color = (random.random(),random.random(),random.random())
		self.goto(x,y)
		self.color(color)
		self.shapesize(radius/10)
		self.radius = radius

