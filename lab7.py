from turtle import *
import random
import turtle
class Ball(Turtle):
	def __init__(self,radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
	def check_colliision
ball_1 = Ball(55,"blue",2)
ball_2 = Ball(30,"red",10)




turtle.mainloop()



