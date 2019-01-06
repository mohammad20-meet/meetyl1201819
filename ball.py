from turtle import *
import random
import math
# turtle.pu()
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
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



