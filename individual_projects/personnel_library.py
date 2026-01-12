#WG_CP1 Personnel library
#import time as t
import time as t
#library with books
library = {"The Hobbit by J.R.R Tolkien", "A Wrinkle in Time by Madeleine L'Engle"}
#define main menu function
def main_menu():
    print("View 1 \nAdd 2  \nRemove 3 \nSearch 4 \nExit 5")

    type = round(float(input("Press the number that is alligned with the calculator you want to use then press enter")), 2)
    print("\033c", end="")
    if type == 1:
        view()
    elif type == 2:
        add()
    elif type == 3:
        remove()
    elif type == 4:
        search()
    elif type == 5:
        exitc()
    else:
        main_menu()
    print("\033c", end="")
#define the view function
def view():
    #print the library
    for i in library:
        print(i)
        t.sleep(3)
    t.sleep(5)
    print("\033c", end="")
#define the add function that adds a book to the library
def add():
    title = input("What is the title of the book.")
    by = input("Who wrote the book?")