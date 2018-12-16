from turtle import *
import random
import turtle
import math
turtle.colormode(255)
#edges
width = 350
height = 350


turtle.pu()
turtle.goto(350,0)
turtle.pd()
turtle.goto(350,350)
turtle.goto(-350,350)
turtle.goto(-350,-350)
turtle.goto(350,-350)
turtle.goto(350,0)
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
	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()		
		newx = oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx,newy)
		if newx>width or newx<-width:
			self.dx = -self.dx
		if newy>height or newy<-height:
			self.dy = -self.dy
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r,g,b)


def check_colliision(ball_1,ball_2):
	x1 = ball_1.xcor()
	x2 = ball_2.xcor()
	y1 = ball_1.ycor()
	y2 = ball_2.xcor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

	if D<ball_1.radius+ball_2.radius:
		return True
	else:
		return False



turtle.bgcolor("pink")
ball_1 = Ball(30,30,50,30,30,"blue")
ball_2 = Ball(50,14,20,40,30,"red")



while True:
	ball_1.move()
	ball_2.move()
	if(check_colliision(ball_1, ball_2) == True):
		ball_1.random_color()
		ball_2.random_color()
turtle.mainloop()



