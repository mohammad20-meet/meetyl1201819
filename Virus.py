import random
from turtle import Turtle



class Virus(Turtle):
	def __init__(self,x,y,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)