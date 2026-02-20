#WG_CP2 Word counter file handling 1st
#import the time getter thing fuction
from helper import current_time, clear_screen
#A function that gets an input on what they want to add and checks if it exists
def create_input(path):
    create = input("What are you adding to the file? please spell exactly the way you want to spell it. ").strip()
    clear_screen()
    add(create, path)

#A function that adds something to the end of a txt with the thing being added at the end of the txt
def add(adding, path):
    with open(path, "a") as file:
        file.write(f"\n{adding}")
        file.write(f"\nThis was updated {current_time()}, and had the word count {word_count(path)}")
#A function that reads through the entire file and loops through the lines adding them to a variable then prints it
def read(path):
    with open(path, "r") as file:
        for line in file:
            print(line)

#A function that reads through the file and increases a variable by one printing it to give them the word count
def word_count(path):
    words = []
    with open(path, "r") as file:
        for line in file:
            words.append(line.split())
    return len(words)
