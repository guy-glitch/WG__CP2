#WG_CP2 Classes project 
from pet_control import *
from login import *

pet = Pet

#main menu function 
def main_menu():
    action = input("Do you want to 1 feed your pet, 2 play with your pet, 3 put your pet to sleep, 4 check your pets status, 5 save your game, 6 load a previous game, 7 exit the game, please input only a number. ").strip()
    #Use case
    match action:
        #case 1 feed
        case "1":
            print()
        #case 2 play
        case "2":
            print()
        #case 3 sleep
        case "3":
            print()
        #case 4 check status
        case "4":
            print()
        #case 5 save
        case "5":
            print()
        #case 6 load
        case "6":
            print()
        #case 7 exit
        case "7":
            print()
        case _:
            print("That input was not an option please try again")
            main_menu()

#call main menu
main_menu()