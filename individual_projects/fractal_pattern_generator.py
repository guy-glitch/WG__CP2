#import turtle
import turtle as t
#Get how many times they want to nest the fractal 
recursions = t.input("How many recursions do you want tod do (1-5)? ")
while True:
    #use try and except to check if it is an integer
    try:
        recursions = int(recursions)
        break
    except:
        recursions = t.input("How many recursions do you want tod do (1-99)? ")
#get them to enter a color
color = t.input("What color do you want the turtle to be? ")
#A while loop that checks if it is possible to set the turtle to that color using try and except and if not asks them again
while True:
    try:
        t.color(color)
        break
    except:
        color = t.input("What color do you want the turtle to be? ")
#Setup the screen 
#define a function that uses turtle to display the fractal inside of itself repeating that many times 
    #do something
    #do something else
    #return something that calls this function in returning it