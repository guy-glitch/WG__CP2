#import time and csv, along with clear screen from login and random
import random as r
import time as t
import csv
from login import clear_screen
types = ["dog","fish","cat","lizard","spider"]

#class Pet
class Pet:
    def __init__():
        #name
        name = input("What do you want to name your pet? ").strip().title()
        
        #type dog, cat, fish, lizard
        while True:
            try:
                type = input(f"What species do you want {name} to be? Your options are dog, cat, fish, lizard, or spider?").strip().lower()
                if type in types:
                    t.sleep(2)
                    clear_screen()
                    break
            except:
                print(f"{type} is not an option for the type.")

        #Age in months
        while True:
            age = input(f"How old in months is {name}? Please input only a number. ").strip()
            try:
                age = int(age)
                break
            except:
                print(f"{age} is not a number. ")
        
        #set their health, energy, happiness, and hunger to a random whole number between 1,100
        energy = r.randint(30,99)
        happiness = r.randint(30,99)
        hunger = r.randint(30,99)
        health = (energy+happiness+hunger)/3
        
        #based off of the user profiles last pet num
        inputFile = "individual_projects\classes\users.csv"
        last_num = open(inputFile, "r")
        last_line = last_num.readlines()[-1]
        last_num.close()
        if last_line is int:
            number = (last_line+1)
        else:
            number = 1
        pet = {"number":number,"name":name,"type":type,"age":age,"health":health,"hunger":hunger,"happiness":happiness,"energy":energy}

#A dictionary of all of the pet types as keys, and within each value have a dictionary of the possible food items for that species and the value it increases stats by
food_options = {"dog":{},"cat":{},"fish":{},"lizard":{},"spider":{}}

#A function that save the pet under its number in the pet status csv
def save(pet):
     pet
     with open("Notes/sample.csv", 'r+', newline='') as csvfile:
        feildnames = ["number", "name","species","age","health","hunger","happiness","energy"]
        writer = csv.DictWriter(csvfile, fieldnames=feildnames)
        writer.writerow({})

#A function that based off of the pet type 

#A function that takes in what food they selected and changes the stats of their pet by that before overwriting their current stats


#A function that increases their stats based off of sleep or play and overwrites their previous stats
