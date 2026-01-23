#WG_CP2 random password generator
#list of characters
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@","#", "$","%", "^","&","*", "(","-", "_","=", "+"]
#import random
import random as r
#import time as t
import time as t
#define main menu function
def main_menu():
    #give the user menu options get which one they want to use, and call the relevant function
    print("\nRandom password 1 \nExit 2")

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
        t.sleep(5)
        main_menu()

#define random password
def rand_pass():
    #inside this get the length of the password from the user and get the character types they want to use using external functions. Then call the password generator function to generate and print 4 passwords.
    length = input("How many characters do you want to be in your password? ")
    print("\033c", end="")

    if length.isdigit():
        length = int(length)
        password = ""
        possible_characters = characters()

        for i in range(4):
            password_gen(length, possible_characters)
        wait = input("Press enter to return to the main menu.")
        print("\033c", end="")
        main_menu()
    
    else:
        print("\033c", end="")
        print("Please input a number.")
        t.sleep(5)
        rand_pass()

#define characters function
def characters():
    #get the character types the user want to have in their password and return a list of possible characters based on the character types they choose.
    if_lower = input("Do you want lowercase letters in your password? (y/n) ")
    if_upper = input("Do you want uppercase letters in your password? (y/n) ")
    if_numbers = input("Do you want numbers in your password? (y/n) ")
    if_symbols = input("Do you want symbols in your password? (y/n) ")
    possible_characters = []
    print("\033c", end="")

    if if_lower.lower() == "y":
        possible_characters += lower
    if if_upper.lower() == "y":
        possible_characters += upper
    if if_numbers.lower() == "y":
        possible_characters += numbers
    if if_symbols.lower() == "y":
        possible_characters += symbols
    if not possible_characters:
        print("You must select at least one character type.")
        characters()
    return possible_characters
#define password generator function
def password_gen(length, possible_characters):
    password = ""
    #based off the length and possible characters generate a random password and print it do this four times.
    for i in range(length):
        password += r.choice(possible_characters)
    print(f"Here is your password option: \n{password}", end="\n\n")
#clear the terminal for aesthetics
print("\033c", end="")
#call main menu
main_menu()