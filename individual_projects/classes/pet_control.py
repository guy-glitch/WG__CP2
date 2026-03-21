
#import time and csv, along with clear screen from login and random
import random as r
import time as t
import csv
from login import clear_screen
types = ["dog","fish","cat","lizard","spider"]

#class Pet
class Pet:
    def __init__(self, num, name, type, age, health, hunger, happiness, energy):
        #name
        self.num = num
        self.name = name
        self.type = type
        self.age = age
        #type dog, cat, fish, lizard
    
        #Age in months
        
        #set their health, energy, happiness, and hunger to a random whole number between 1,100
        self.energy = r.randint(30,99)
        self.happiness = r.randint(30,99)
        self.hunger = r.randint(30,99)
        self.health = (self.energy+self.happiness+self.hunger)/3
        


#define a function called create_pet that takes in the users input for the name, type, and age of their pet and creates a pet object with those values and the rest being random then saves it to the csv
def create_pet():
    name = input("What would you like to name your pet? ").strip()
    clear_screen()
    type = input("What type of pet would you like? (dog, cat, fish, lizard, spider) ").strip().lower()
    clear_screen()
    age = int(input("How old is your pet in months? ").strip())
    clear_screen()
    energy = r.randint(30,99)
    clear_screen()
    happiness = r.randint(30,99)
    clear_screen()
    hunger = r.randint(30,99)
    clear_screen()
    health = (energy+happiness+hunger)/3
    try:
        with open("individual_projects//classes//pet_status.csv", 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            nums = [row[7] for row in reader if row]
            nums.remove("number")
            nums = [int(num) for num in nums]
            num = max(nums) + 1 if nums else 1
    except FileNotFoundError:
        num = 1
    pet = Pet(num,name,type,age,health,hunger,happiness,energy)
    save(pet)
    return pet
#A function that save the pet under its number in the pet status csv
def save(pet):
    with open("individual_projects//classes//pet_status.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([pet.name, pet.type, pet.age, pet.health, pet.hunger, pet.happiness, pet.energy, pet.num])

#A function that based off of the pet type gives them options for food and how much it increases their stats by, then calls the function to change their stats based on the food they selected arguments are pet
def feeding(pet):
        
        if pet["type"] == "dog":
            print("You can feed your dog: 1. Dog food (hunger +10, happiness -10, energy +10), 2. Steak (hunger +20, happiness +20, energy +2), 3. Ice cream (hunger -5, happiness +5, energy +5, health -5)")
            food = input("What would you like to feed your dog? ").strip()
        
            match food:
        
                case "1":
                    pet["hunger"] += 10
                    pet["happiness"] -= 10
                    pet["energy"] += 10
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "2":
                    pet["hunger"] += 20
                    pet["happiness"] += 20
                    pet["energy"] += 2
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "3":
                    pet["hunger"] -= 5
                    pet["happiness"] += 5
                    pet["energy"] += 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3 - 5
                    print("Status updated!")
                    clear_screen()
                
                case _:
                    print("That is not an option, please try again.")
                    feeding(pet)
        
        elif pet["type"] == "cat":
            print("You can feed your cat: 1. Cat food (hunger +30, energy +10, happiness -10), 2. Fish (hunger +15, happiness +15, energy +15), 3. Milk (hunger +5, happiness +5, energy -5, health -5)")
            food = input("What would you like to feed your cat? ").strip()
        
            match food:
        
                case "1":
                    pet["hunger"] += 30
                    pet["happiness"] -= 10
                    pet["energy"] += 10
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "2":
                    pet["hunger"] += 15
                    pet["happiness"] += 15
                    pet["energy"] += 15
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "3":
                    pet["hunger"] += 5
                    pet["happiness"] += 5
                    pet["energy"] -= 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3 - 5
                    print("Status updated!")
                    clear_screen()
                case _:
                    print("That is not an option, please try again.")
                    feeding(pet)
        
        elif pet["type"] == "fish":
            print("You can feed your fish: 1. Fish flakes (hunger +10, happiness -10, energy +10), 2. Worms (hunger +20, happiness +15, energy +5), 3. Bread (hunger +20, happiness +5, energy +5, health -7)")
            food = input("What would you like to feed your fish? ").strip()
        
            match food:
        
                case "1":
                    pet["hunger"] += 10
                    pet["happiness"] -= 10
                    pet["energy"] += 10
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "2":
                    pet["hunger"] += 20
                    pet["happiness"] += 15
                    pet["energy"] += 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "3":
                    pet["hunger"] += 20
                    pet["happiness"] += 5
                    pet["energy"] += 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3 - 7
                    print("Status updated!")
                    clear_screen()
                case _:
                    print("That is not an option, please try again.")
                    feeding(pet)
        
        elif pet["type"] == "lizard":
            print("You can feed your lizard: 1. Crickets (hunger +10, happiness -10, energy +10), 2. Mealworms (hunger +15, happiness +20, energy +5), 3. Fruit (hunger +10, happiness +10, energy -5, health -5)")
            food = input("What would you like to feed your lizard? ").strip()
        
            match food:
        
                case "1":
                    pet["hunger"] += 10
                    pet["happiness"] -= 10
                    pet["energy"] += 10
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()

                case "2":
                    pet["hunger"] += 15
                    pet["happiness"] += 20
                    pet["energy"] += 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()

                case "3":
                    pet["hunger"] += 10
                    pet["happiness"] += 10
                    pet["energy"] -= 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3 - 5
                    print("Status updated!")
                    clear_screen()

                case _:
                    print("That is not an option, please try again.")
                    feeding(pet)
        
        elif pet["type"] == "spider":
            print("You can feed your spider: 1. Flies (hunger +10, happiness -10, energy +10), 2. Moths (hunger +20, happiness +15, energy +5), 3. Sugar (hunger +5, happiness +5, energy -5, health -5)")
            food = input("What would you like to feed your spider? ").strip()
        
            match food:
        
                case "1":
                    pet["hunger"] += 10
                    pet["happiness"] -= 10
                    pet["energy"] += 10
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()        
                case "2":
                    pet["hunger"] += 20
                    pet["happiness"] += 15
                    pet["energy"] += 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
                    print("Status updated!")
                    clear_screen()
                case "3":
                    pet["hunger"] += 5
                    pet["happiness"] += 5
                    pet["energy"] -= 5
                    pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3 - 5
                    print("Status updated!")
                    clear_screen()
        
                case _:
                    print("That is not an option, please try again.")
                    feeding(pet)
        save(pet)

#A function that increases their stats based off of sleep or play and overwrites their previous stats
def sleep_play(pet, sleeporplay):
    if sleeporplay == "sleep":
        pet["energy"] += 20
        pet["happiness"] += 10
        pet["hunger"] -= 10
        pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
    elif sleeporplay == "play":
        pet["energy"] -= 30
        pet["happiness"] += 20
        pet["hunger"] -= 10
        pet["health"] = (pet["energy"]+pet["happiness"]+pet["hunger"])/3
    save(pet)