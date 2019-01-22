import turtle
import time
import random
import keyboard
from ball import *
from dots import *
from Virus import *
RUNNING = True
turtle.tracer(0, 0)
turtle.hideturtle()
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

My_BALL =  Ball(0,0,0,0,20,"green")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

NUMBER_OF_Dots = 120
MINIMUM_Dot_RADIUS = 5
MAXIMUM_Dot_RADIUS = 5
NUMBER_OF_Viruss = 3 
MINIMUM_Virus_RADIUS = 60
MAXIMUM_Virus_RADIUS = 65
turtle.bgcolor("white")
My_BALLS = []
BALLS = []
Dots = []
Viruss = []

def split_ball(radius):

	if My_BALL.radius> 30:
		My_BALL.radius = radius
		My_BALL.shapesize(My_BALL.radius/10)
		return True
	else:
		return False
SPACEBAR = "space"
def check_space():
		if keyboard.is_pressed("space"): #check if you pressed the space bar
			print ("SOMETHING HAPPENED")
			if split_ball(My_BALL.radius/2) == True:
			#SSS = Ball(x,y,dx,dy,radius,color)
				BBB1 = My_BALL.clone()
			#My_BALLS.append(SSS)

#shoot the other ball 10 pixels away "cursor direction" then make the clone the exact same as my_ball then
#make a function called dont touch which calculates the radius between ur ball and the clone and if its
#colling make ASK AJA






for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

for i in range(NUMBER_OF_Dots):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_Dot_RADIUS,SCREEN_WIDTH - MAXIMUM_Dot_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_Dot_RADIUS,SCREEN_HEIGHT - MAXIMUM_Dot_RADIUS)
	radius = random.randint(MINIMUM_Dot_RADIUS,MAXIMUM_Dot_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_Dots = Dot(x,y,radius,color)
	Dots.append(new_Dots)

for i in range(NUMBER_OF_Viruss):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_Virus_RADIUS,SCREEN_WIDTH - MAXIMUM_Virus_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_Virus_RADIUS,SCREEN_HEIGHT - MAXIMUM_Virus_RADIUS)
	radius = random.randint(MINIMUM_Virus_RADIUS,MAXIMUM_Virus_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_Virus = Virus(x,y,radius,color)
	Viruss.append(new_Virus)
#Function to control My_BALL
def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y
	My_BALL.dx = (x - My_BALL.xcor()) / 50
	My_BALL.dy = (y - My_BALL.ycor()) / 50
	# My_BALL.goto(x,y)
turtle.getcanvas().bind("<Motion>", movearound)


def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		i.speed()
def collide1(ball_a,ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D<ball_a.radius+ball_b.radius:
		return True
	else:
		return False
#Bot balls colliding definition
def collide(ball_a,ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D+10<ball_a.radius+ball_b.radius:
		return True
	else:
		return False
#My_BALL eating / teleporting 

def check_myball_collision():
	for ball_D in BALLS:
		if collide(My_BALL,ball_D):
			if My_BALL.radius>ball_D.radius:
				My_BALL.grow(ball_D.radius/6)
				ball_D.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
			elif ball_D.radius > My_BALL.radius:
				ball_D.grow(ball_D.radius/6)
				quit()
	for DOT in Dots:
		if collide1(My_BALL,DOT):
			My_BALL.grow(DOT.radius/20)
			DOT.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)


#Bot balls colliding code "eating / teleporting "
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):
				if ball_a.radius> ball_b.radius:
					ball_a.grow(ball_b.radius/6)
					ball_b.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				elif ball_b.radius>ball_a.radius:
					ball_b.grow(ball_a.radius/5)
					ball_a.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
		for DOT in Dots:
			if collide1(ball_a, DOT):
				ball_a.grow(DOT.radius/20)
				DOT.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)

while RUNNING is True:
	#for ball in BALLS:
	#	ball.speed()
	My_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	move_all_balls()
	check_space()
	check_myball_collision()
	time.sleep(SLEEP)
	check_all_balls_collision()
	turtle.update()