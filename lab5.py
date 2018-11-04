'''
import tkinter as tk
from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ("Arrr!"):
    print("Go away, pirate.")
else:
	 print("Greetings, hater of pirates!")

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

import tkinter as tk
from tkinter import simpledialog

year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 2021:
    print ("Far out, that's the future!!")

else:
    print ("That's totally the present!")
    


    
class Person(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	def speak(self):
		print("My name is " +  self.first_name + " " + self.last_name)
me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
'''

import tkinter as tk
from tkinter import simpledialog
# Grade: F
# Student iis failing.

exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = simpledialog.askstring("Input"," exam grade two: ", parent=tk.Tk().withdraw())

exam_three = str(simpledialog.askstring("Input", "exam grade three: "), parent=tk.Tk().withdraw())


grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
   print ("Student is failing.")
else:
    print ("Student is passing.")

