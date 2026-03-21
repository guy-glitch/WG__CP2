#WG_CP2 Classes project 
import random as r
from pet_control import *
from login import *
clear_screen()

random_event = [{"cause":"Found a bone in the forest", "effect":"Your pet gains 10 happiness!", "change":"happiness", "value": 10},{"cause":"Ate its own puke", "effect":"Your pet loses 10 happiness!", "change":"happiness", "value": -10},{"cause": "Didn't want to eat", "effect":"Your pet loses 10 hunger!", "change":"hunger", "value": -10},{"cause":"Your pet aged a month", "effect":"Your pet's age has increased!", "change":"age", "value": 1}]

def start():
    pet = create_pet()
    print(f"Congratulations on your new pet {pet.name} the {pet.type}!")
    main_menu(pet)

#main menu function 
def main_menu(pet):
    while True:
        clear_screen()
        action = input("Do you want to\n1 feed your pet,\n2 play with your pet,\n3 put your pet to sleep,\n4 check your pets status,\n5 save your game,\n6 load a previous game,\n7 exit the game, please input only a number. ").strip()
        #Use case
        match action:
            
            #case 1 feed
            case "1":
                pet = feeding(pet)
            
            #case 2 play
            case "2":
                pet = sleep_play(pet, "play")
            
            #case 3 sleep
            case "3":
                pet = sleep_play(pet, "sleep")
            
            #case 4 check status
            case "4":
                print(f"Your pet's name is {pet.name}, they are a {pet.age} year old {pet.type}. Their health is at {pet.health}, their hunger is at {pet.hunger}, their happiness is at {pet.happiness}, and their energy is at {pet.energy}.")
            
            #case 5 save
            case "5":
                save_pet()
            
            #case 6 load
            case "6":
                pet = login()
                print(f"Welcome back your pet has been changed to {pet['name']} the {pet['species']}!")
            
            #case 7 exit
            case "7":
                exit()
            case _:
                print("That input was not an option please try again")
        event = r.choice(random_event)
        print(f"Random event: {event['cause']} {event['effect']}")
        if event["change"] == "happiness":
            pet.happiness += event["value"]
        elif event["change"] == "hunger":
            pet.hunger += event["value"]
        elif event["change"] == "age":
            pet.age += event["value"]
        elif event["change"] == "health":
            pet.health += event["value"]
#call main menu
start()