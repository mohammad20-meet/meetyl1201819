'''
import turtle
from turtle import Turtle
import random
turtle.colormode(255)
class Square(Turtle):
	def __init__(self,size,):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r,g,b)


square1 = Square(5)
square1.random_color()


turtle.mainloop()

#do extras
'''
from turtle import Turtle
import turtle
turtle.begin_poly()
import turtle
turtle.pu()
turtle.forward(50)
for i in range(6):
	turtle.pd()
	turtle.right(60)
	turtle.forward(50)
turtle.end_poly()
turtle.register_shape("potato",(turtle.get_poly()))

class Hexagon(Turtle):
	def __init__(self,size):
		self.shapesize(size)
		self.shape(potato)

turtle.mainloop()

hexagon1 = Hexagon(99)





