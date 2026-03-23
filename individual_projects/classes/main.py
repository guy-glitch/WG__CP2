#WG_CP2 Classes project 
import random as r
from pet_control import *
from login import *
clear_screen()

random_event = [
    {"cause":"Found a bone in the forest", "effect":"Your pet gains 10 happiness!", "change":"happiness", "value": 10},
    {"cause":"Ate its own puke", "effect":"Your pet loses 10 happiness!", "change":"happiness", "value": -10},
    {"cause": "Didn't want to eat", "effect":"Your pet loses 10 hunger!", "change":"hunger", "value": -10},
    {"cause":"Your pet aged a month", "effect":"Your pet's age has increased!", "change":"age", "value": 1},
    {"cause":"Your pet got sick", "effect":"Your pet loses 20 health!", "change":"health", "value": -20}
]

def apply_random_event(pet):
    event = r.choice(random_event)
    print(f"Random event: {event['cause']} {event['effect']}")
    if event["change"] == "happiness":
        pet.happiness = max(0, min(100, pet.happiness + event["value"]))
    elif event["change"] == "hunger":
        pet.hunger = max(0, min(100, pet.hunger + event["value"]))
    elif event["change"] == "age":
        pet.age += event["value"]
    elif event["change"] == "health":
        pet.health = max(0, min(100, pet.health + event["value"]))
    pet.update_health()

def start():
    pets = []  # list of pets
    pet = create_pet()
    pets.append(pet)
    current_pet_index = 0
    print(f"Congratulations on your new pet {pet.name} the {pet.species}!")
    main_menu(pets, current_pet_index)

#main menu function 
def main_menu(pets, current_pet_index):
    while True:
        pet = pets[current_pet_index]
        if pet.health <= 0:
            print("Your pet has died. Please make a new pet. ")
            pets.remove(pet)
            start()
        elif pet.energy <= 0:
            print("Your pet has died. Please make a new pet. ")
            pets.remove(pet)
            start()
        elif pet.happiness <= 0:
            print("Your pet has died. Please make a new pet. ")
            pets.remove(pet)
            start()
        elif pet.hunger <= 0:
            print("Your pet has died. Please make a new pet. ")
            pets.remove(pet)
            start()
        else:

            clear_screen()
            action = input(f"Do you want to\n1 feed your pet ({pet.name}),\n2 play with your pet,\n3 put your pet to sleep,\n4 check your pets status,\n5 create a new pet,\n6 switch pet,\n7 save your game,\n8 load a previous game,\n9 exit the game, please input only a number. ").strip()
            #Use case
            match action:
                
                #case 1 feed
                case "1":
                    pet.feed()
                    apply_random_event(pet)
                
                #case 2 play
                case "2":
                    pet.play()
                    print("You played with your pet!")
                    apply_random_event(pet)
                
                #case 3 sleep
                case "3":
                    pet.sleep()
                    print("Your pet slept!")
                    apply_random_event(pet)
                
                #case 4 check status
                case "4":
                    pet.display_status()
                    input("Press enter to continue...")
                
                #case 5 create new pet
                case "5":
                    new_pet = create_pet()
                    pets.append(new_pet)
                    current_pet_index = len(pets) - 1
                    print(f"Congratulations on your new pet {new_pet.name} the {new_pet.species}!")
                
                #case 6 switch pet
                case "6":
                    if len(pets) > 1:
                        print("Your pets:")
                        for i, p in enumerate(pets):
                            print(f"{i+1}. {p.name} the {p.species}")
                        choice = int(input("Which pet do you want to switch to? ")) - 1
                        if 0 <= choice < len(pets):
                            current_pet_index = choice
                            print(f"Switched to {pets[current_pet_index].name}!")
                        else:
                            print("Invalid choice.")
                    else:
                        print("You only have one pet.")
                
                #case 7 save
                case "7":
                    save_pet(pet)
                
                #case 8 load
                case "8":
                    loaded_pet = login()
                    pets.append(loaded_pet)
                    current_pet_index = len(pets) - 1
                    print(f"Welcome back your pet {loaded_pet.name} the {loaded_pet.species}!")
                
                #case 9 exit
                case "9":
                    exit()
                case _:
                    print("That input was not an option please try again")
#call main menu
start()