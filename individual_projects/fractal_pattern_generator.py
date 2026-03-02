#import turtle
import turtle as t
import time 
print("Welcome to the fractal generator!")
#Get how many times they want to nest the fractal 
recursions = input("How many recursions do you want to do (1-7)? ").strip()

while True:
    #use try and except to check if it is an integer

    try:
        recursions = int(recursions)
        break

    except:
        recursions = input("How many recursions do you want tod do (1-7)? ")
recursions = int(recursions)
#get them to enter a color
color = input("What color do you want the turtle to be? ").strip().lower()

#A while loop that checks if it is possible to set the turtle to that color using try and except and if not asks them again
while True:

    try:
        t.color(color)
        break

    except:
        color = input("What color do you want the turtle to be? ")

#Setup the screen 
screen = t.Screen()
background = input("What color do you want the background to be? ")
while True:

    try:
        screen.bgcolor(background)
        break

    except:
        background = input("What color do you want the background to be? ")
screen.setup(1000,1000)

#hide the turtle
t.hideturtle()

#A function that calls the function multiple times
def poly_call(number, startx, starty, size):
    #return something that calls this function in returning it
    fractal(number-1, startx, starty, size/2)
    fractal(number-1, startx + size/2, starty, size/2)
    fractal(number-1, startx + size/4, starty + size*0.4355, size/2)

#increase speed
t.speed(0)
base = -350
#define a function that uses turtle to display the fractal inside of itself repeating that many times 
def fractal(number, startx, starty, size):
    t.tracer(0,0)
    #create a base case
    if number == 0: return
    #set the turtle to a position
    t.teleport(startx, starty)
    #draw a triangle
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    
    #return something that calls this function in returning it
    poly_call(number, startx, starty, size)

fractal(recursions, base, base, 500)
t.update
t.done()