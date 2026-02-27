#import turtle
import turtle as t
import time 

#Get how many times they want to nest the fractal 
recursions = input("How many recursions do you want tod do (1-5)? ")

while True:
    #use try and except to check if it is an integer

    try:
        recursions = int(recursions)
        break

    except:
        recursions = input("How many recursions do you want tod do (1-99)? ")
recursions = int(recursions)
#get them to enter a color
color = input("What color do you want the turtle to be? ")

#A while loop that checks if it is possible to set the turtle to that color using try and except and if not asks them again
while True:

    try:
        t.color(color)
        break

    except:
        color = input("What color do you want the turtle to be? ")

#Setup the screen 
screen = t.Screen()
screen.setup(1000,1000)

#hide the turtle
t.hideturtle()

#increase speed
t.speed(0)
base = -350
#define a function that uses turtle to display the fractal inside of itself repeating that many times 
def fractal(number):

    #create a base case
    if number == 0: return 0
    #set the turtle to a position
    t.teleport(base, base)
    #use a for loop base off of the number 
    t.forward(900/((number+1)*2))
    t.left(120)
    t.forward(900/((number+1)*2))
    t.left(120)
    t.forward(900/((number+1)*2))
    t.left(120)
    
    #return something that calls this function in returning it
    return fractal(number-1)
fractal(recursions)
time.sleep(15)
t.done()