#WG_CP2 random password generator
#list of characters
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
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
def rand_pass():
    #inside this
    length = input("How many characters do you want to be in your password? ")
    if length.isdigit():
        length = int(length)
        password = ""
        for i in range(length):
            password += r.choice(characters)
        print(f"Your random password is: {password}")
        t.sleep(20)
        print("\033c", end="")
        main_menu()
    else:
        print("\033c", end="")
        print("Please input a number.")
        t.sleep(20)
        rand_pass()
main_menu()