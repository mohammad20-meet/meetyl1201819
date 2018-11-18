'''
print ("Mohammad")





number1 = 200
number2 = 100
number3 = 50

for i in range (1):
	print (number1 * 2)
	print (number2 * 2)
	print (number3 * 2)
print ((number1 + number2+ number3)* 2)
'''
'''
import turtle
turtle.goto(100,100)







turtle.mainloop()
'''
import turtle
turtle.pensize(10)
radius = 100
def draw_circle(color,x,y):
	turtle.pu()
	turtle.color(color)
	turtle.goto(x,y)
	turtle.pd()
	turtle.circle(radius)
draw_circle("blue",250,0)
draw_circle("black",0,0)
draw_circle("red",-250,0)
draw_circle("yellow",-130,-100)
draw_circle("green",130,-100)
turtle.mainloop()
