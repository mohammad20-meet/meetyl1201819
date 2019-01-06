from turtle import *
import random
import turtle
import math
turtle.colormode(255)
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		#self.speed(speed)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r,g,b)
turtle.bgcolor("pink")
ball_1 = Ball(30,30,50,30,30,random_color())
ball_2 = Ball(50,14,20,40,30,random_color())
turtle.mainloop()