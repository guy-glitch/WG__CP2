#WG_CP1 Personnel library
import csv
#import time as t
import time as t
#library with books
try:
    with open("individual_projects/library.csv", mode = "r") as library:
        content = csv.reader(library)
        headers = next(content)
        library = []
        for line in content:
           library.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3]})

except:
    print("The library is having trouble loading please close and try again.")
    exit()

#define main menu function
def main_menu(library):
    #use match to let them check if they choose to enter the morse code translator
    while True:
        print("View 1 \nAdd 2  \nRemove 3 \nSearch 4 \nExit 5")
        type = input("Press the number that is alligned with the library function you want to use then press enter? ")        
        match type:
            case "1":
                print("\033c", end="")
                display(library)
            case "2":
                print("\033c", end="")
                add(library)
            case "3":
                print("\033c", end="")
                remove(library)
            case "4":
                print("\033c", end="")
                search(library)
            case "5":
                print("\033c", end="")
                exit()
            case _:
                print("Input is not an option")
                t.sleep(3)
                print("\033c", end="")
                continue

#define a function that displays everything in the vile
def display(library):
    exit = 1
    while exit!="y":
        view(library)
        exit = input("Do you want to exit. y/n")
    return exit

#define the view function
def view(library):
    for i in range(len(library)):
        if isinstance(library[i], dict):
            for j in library[i]:
                print(f"{j}:{library[i][j]}", end=" ")
        print()
    exit = input("Do you want to exit only enter something if you want to exit. ")
    print("\033c", end="")
    main_menu(library)

#define the add function that adds a book to the library
def add(library):
    #get the title and the author than add it to the library
    title = input("What is the title of the book. ").strip().title()
    by = input("Who wrote the book? ").strip().title()
    year = input("When was this book published? ")
    genre = input("What is the genre of the book?")
    book = {"title":title, "author":by}
    library.append(book)

    print(f"{book} added to the library")
    print("\033c", end="")
    main_menu(library)
#define the function that removes a book from the library

def remove(library):
    title = input("What is the title or author of the book you want to remove? ").strip().title()
    in_library = any(title in item for item in library)

    if in_library:
        for book in library:
            if title in book:
                library.discard(book)
                print(f"{book} has been removed from the library. ")
                t.sleep(3)
                print("\033c", end="")
                main_menu(library)

    else:
        print(f"{title} is not in the library, make sure it is spelled correctly next time. ")
        print("\033c", end="")
        main_menu(library)

#define a function that allows for you to search the library

def search(library):
    title = input("What do you want to search for in the library? ").title().strip()
    in_library = any(title in item for item in library)

    if in_library:

        for book in library:

            if title in book:
                print(f"{book} is in the library.")
                t.sleep(5)
                print("\033c", end="")
                main_menu(library)
    else:
        print(title, " is not in the library")

    main_menu()

#define a function that exits the program
def exitp():
    print("Okay! See you soon.")

    t.sleep(2)
    print("\033c", end="")
    quit()

main_menu(library)