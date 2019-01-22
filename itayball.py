import turtle
from turtle import Turtle
import math



class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.shapesize(self.r/10)
		self.penup()
		self.goto(x,y)
		self.shape("circle")
	def move(self, screen_width, screen_height):
		
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		self.goto(new_x, new_y)