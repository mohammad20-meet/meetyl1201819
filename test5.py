import turtle
import time
import random  #For the Random Spawn locations
#import keyboard #For the Split part
from ball import * 
from dots import *
from Virus import *
RUNNING = True
turtle.tracer(0, 0)
turtle.hideturtle()
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

My_BALL =  Ball(0,0,0,0,150,"green")

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

#turtle.register_shape("virus.gif")
#turtle.
#Lists
My_BALLS = []
BALLS = []
Dots = []
Viruss = []

My_BALLS.append(My_BALL)

#turtle.register_shape("virus.gif")
#Virus.shape("virus.gif")


def split_ball(radius):
	
	if radius> 30:
		return True
	else:
		return False
SPACEBAR = "space"
def check_space():
	global My_BALLS
	print ("SOMETHING HAPPENED")
	NEW_BALLS = []
	for Half in My_BALLS:
		if split_ball(Half.radius/2) == True:
			print("big enough")
			Half.radius = Half.radius/2
			Half.shapesize(Half.radius/10)
			New_Half = Half.clone()
			NEW_BALLS.append(New_Half)
			Half.goto(Half.dx*20 +Half.xcor(),Half.dy*20 + Half.ycor())
	My_BALLS = My_BALLS+NEW_BALLS
	run_game()


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
	for Half in My_BALLS:
		x = event.x - SCREEN_WIDTH
		y = SCREEN_HEIGHT - event.y
		Half.dx = (x - Half.xcor()) / 30
		Half.dy = (y - Half.ycor()) / 30
	#	for Half in My_BALLS:
	#		Half.dx = My_BALL.dx
	#		Half.dy = My_BALL.dy
turtle.getcanvas().bind("<Motion>", movearound)
turtle.onkeypress(check_space,"space")
turtle.listen()
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		i.speed()

def No_Touching():
	global My_BALLS
	NEW_BALLS = []
	disappear = []
	for i in range(0, len(My_BALLS)):
		for j in range(i, len(My_BALLS)):
			Half = My_BALLS[i]
			Half2 = My_BALLS[j]
			if collide_Half(Half,Half2) and i not in disappear and j not in disappear:
				Half.grow(Half2.radius)
				Half2.radius = 0
				Half2.ht()
				disappear.append(j)
	for i in range(len(My_BALLS)):
		if i not in disappear:
			NEW_BALLS.append(My_BALLS[i])
	My_BALLS = NEW_BALLS
	
def collide_Half(ball_a,ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D-2<ball_a.radius+ball_b.radius:
		return True
	else:
		return False

def collide_Dot(ball_a,ball_b):
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
def collide_Ball(ball_a,ball_b):
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
#Checks my balls collsion
def check_myball_collision():
	for Half in My_BALLS:
		for ball_D in BALLS:
			if collide_Ball(Half,ball_D):
				if Half.radius>ball_D.radius:
					Half.grow(ball_D.radius/5)
					ball_D.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				elif ball_D.radius > Half.radius:
					ball_D.grow(ball_D.radius/5)
					quit()

		for DOT in Dots:
			if collide_Dot(Half,DOT):
				Half.grow(DOT.radius/20)
				DOT.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
		for V in Viruss:
			if collide_Ball(Half, V):
				if Half.radius> V.radius:
					Half.radius= Half.radius/2
					Half.shapesize(Half.radius/10)
					V.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				if Half.radius<V.radius:
					pass

#Bot balls colliding code "eating / teleporting "
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide_Ball(ball_a, ball_b):
				if ball_a.radius> ball_b.radius:
					ball_a.grow(ball_b.radius/5)
					ball_b.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				elif ball_b.radius>ball_a.radius:
					ball_b.grow(ball_a.radius/5)
					ball_a.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
		for DOT in Dots:
			if collide_Dot(ball_a, DOT):
				ball_a.grow(DOT.radius/20)
				DOT.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
		for V in Viruss:
			if collide_Ball(ball_a, V):
				if ball_a.radius> V.radius:
					ball_a.radius = ball_a.radius/2
					ball_a.shapesize(ball_a.radius/10)
					V.thxforplaying(SCREEN_WIDTH,SCREEN_HEIGHT)
				if ball_a.radius<V.radius:
					pass

def run_game():
	#Function caller
	while RUNNING is True:
		for Half in My_BALLS:
			Half.move(SCREEN_WIDTH, SCREEN_HEIGHT)
		#SOMETHING()
		move_all_balls()
		# check_space2()
		check_myball_collision()
		time.sleep(SLEEP)
		No_Touching()
		check_all_balls_collision()
		turtle.update()
run_game()