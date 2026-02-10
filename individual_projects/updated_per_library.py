#WG_CP1 Personnel library
#import time as t
import time as t
#library with books
library = {"The Hobbit by J.R.R Tolkien", "A Wrinkle in Time by Madeleine L'Engle"}

#define main menu function
def main_menu():
    print("View 1 \nAdd 2  \nRemove 3 \nSearch 4 \nExit 5")
    type = input("Press the number that is alligned with the library function you want to use then press enter? ")
    #use match to let them check if they choose to enter the morse code translator
    while True:
        print("View 1 \nAdd 2  \nRemove 3 \nSearch 4 \nExit 5")
        type = input("Press the number that is alligned with the library function you want to use then press enter? ")        
        match type:
            case "1":
                print("\033c", end="")
                ()
            case "2":
                print("\033c", end="")
                ()
            case "3":
                print("\033c", end="")
                exit()
            case _:
                print("Input is not an option")
                t.sleep(3)
                print("\033c", end="")
                continue
    else:
        print("\033c", end="")
        print("Please input a number.")
        t.sleep(20)
        main_menu()

#define the view function
def view():

    #print the library
    for i in library:
        print(i)
        print("")
        t.sleep(3)
   
    print("\033c", end="")
    main_menu()
#define the add function that adds a book to the library

def add():
    #get the title and the author than add it to the library
    title = input("What is the title of the book.").strip().title()
    by = input("Who wrote the book?").strip().title()
    book = f"{title} by {by}"
    library.add(book)

    print(f"{book} added to the library")
    print("\033c", end="")
    main_menu()
#define the function that removes a book from the library

def remove():
    title = input("What is the title or author of the book you want to remove? ").strip().title()
    in_library = any(title in item for item in library)

    if in_library:
        for book in library:
            if title in book:
                library.discard(book)
                print(f"{book} has been removed from the library. ")
                t.sleep(3)
                print("\033c", end="")
                main_menu()

    else:
        print(f"{title} is not in the library, make sure it is spelled correctly next time. ")
        print("\033c", end="")
        main_menu()

#define a function that allows for you to search the library

def search():
    title = input("What do you want to search for in the library? ").title().strip()
    in_library = any(title in item for item in library)

    if in_library:

        for book in library:

            if title in book:
                print(f"{book} is in the library.")
                t.sleep(5)
                print("\033c", end="")
                main_menu()
    else:
        print(title, " is not in the library")

    main_menu()

#define a function that exits the program
def exitp():
    print("Okay! See you soon.")

    t.sleep(2)
    print("\033c", end="")
    quit()

main_menu()