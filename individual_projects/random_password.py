#WG_CP2 random password generator
#list of characters

#import random
import random as r
#import time as t
import time as t
#define main menu function
def main_menu():
    print("Random password 1 \nExit 2")

    type = input("Press the number that is alligned with the library function you want to use then press enter? ")
    if type.isdigit():
        type = int(type)
        print("\033c", end="")
        if type == 1:
            rand_pass()
        elif type == 2:
            exit()
        else:
            main_menu()
    else:
        print("\033c", end="")
        print("Please input a number.")
        t.sleep(20)
        main_menu()

#define random password
    #inside this