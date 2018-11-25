'''
from turtle import Turtle
import turtle
turtle.begin_poly()
import turtle
turtle.pd()
turtle.register_shape("Joyce",(turtle.get_poly()))
for i in range(2000):
	turtle.forward(90)
	turtle.right(45+i)
	turtle.forward(40)
	turtle.home()
turtle.mainloop()


turtle.end_poly()


class Hello(Turtle):
	def __init__(self,size,color):
		self.shapecolor(color)
		self.shapesize(size)
		self.shape(Joyce)
Ahmad = Hello(3)
'''
import turtle
turtle.speed(0)
for i in range(2000):
	turtle.forward(90)
	turtle.right(45+i)
	turtle.forward(40+i)
	turtle.home()
turtle.mainloop()


