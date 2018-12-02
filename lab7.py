from turtle import *
import random
import turtle
import math
colors = ["blue","green","red"]
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius, color):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		#self.speed(speed)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()		
		newx = oldx + self.dx
		newy = newy + self.dy
		self.goto(newx,newy)
def check_colliision(ball_1,ball_2):
	d=math.sqrt(math.pow(x2-x1),2) + math.pow((y2-y1))
	if d<ball_1.radius+ball_2.radius:
		return True
	else:
		return False

ball_1 = Ball(50,30,50,30,15,"red")
ball_2 = Ball(50,14,20,40,15,"blue")
'''
if(check_colliision(ball_1, ball_2) == True):
	random_color = colors.choice()
	ball_1.color(random_color)
	ball_2.color(random_color)
'''

turtle.mainloop()



