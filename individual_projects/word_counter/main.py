# WG_CP2 Word counter main file 1st
#import all of the needed functions from other things
from file_handler import *
from helper import *
#a function that gets what they want to do and calls the releveant function
def main():
    #get there action
    action = input("--- Document Word Count Updater ---" \
    "               1. Update document info" \
    "               2. View document" \
    "               3. Add content to document" \
    "               4. Exit" \
    "               Enter your choice (1-4): 1")
    #match the action
    match action:
        #Call the actions that they chose
        case "1":

        case "2":

        case "3":
            
        case "4":
            exit()