from turtle import *
import random
import turtle
import math
turtle.pu()
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
		turtle.pu()
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

ball_1 = Ball(30,30,50,30,30,"blue")
ball_2 = Ball(50,14,20,40,30,"red")




turtle.mainloop()