# WG_CP2 Word counter main file 1st
#import all of the needed functions from other things
from file_handler import *
from helper import *
#a function that gets what they want to do and calls the releveant function
def main():
    while True:
        path = input("Please enter the relative path of your file with the forward slash turned into backslash thankyou. ").strip()
        #get there action
        action = input("--- Document Word Count Updater ---\n" 
        "1. View document\n"
        "2. Add content to document\n" 
        "3. Exit\n"
        "Enter your choice (1-3): ").strip()
        clear_screen()
        #match the action
        match action:
            #Call the actions that they chose
            case "1":
                read(path)
            case "2":
                create_input(path)
            case "3":
                exit()
            case _:
                print("Incorrect input please try again")
                clear_screen()
#call main
main()