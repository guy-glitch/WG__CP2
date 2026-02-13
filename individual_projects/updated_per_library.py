#WG_CP1 Personnel library
import csv
#import time as t
import time as t
#define clear screen function
def clear_screen():
    print("\033c", end="")
#library with books
try:
    with open("individual_projects/library.csv", mode = "r") as library:
        content = csv.DictReader(library)
        headers = content.fieldnames
        library = []
        for line in content:
           library.append({headers[0]: line[headers[0]], headers[1]: line[headers[1]], headers[2]: line[headers[2]], headers[3]: line[headers[3]]})

except:
    print("The library is having trouble loading please close and try again.")
    exit()

def save_library(library):
    try:
        with open("individual_projects/library.csv", mode="w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for item in library:
                writer.writerow(item)
    except:
        print("Failed to save library. Please close and try again.")

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
    for item in library:
        if isinstance(item, dict):
            for k, v in item.items():
                print(f"{k}: {v}", end=" ")
        print()
    _ = input("Do you want to exit only enter something if you want to exit. ")
    clear_screen()
    main_menu(library)

#define the add function that adds a book to the library
def add(library):
    title = input("What is the title of the book. ").strip().title()
    by = input("Who wrote the book? ").strip().title()
    year = input("When was this book published? ")
    genre = input("What is the genre of the book?")
    book = {headers[0]: title, headers[1]: by, headers[2]: year, headers[3]: genre}
    library.append(book)
    save_library(library)
    print(f"{book} added to the library")
    print("\033c", end="")
    main_menu(library)

#define the function that removes a book from the library
def remove(library):
    term = input("What is the title or author of the book you want to remove? ").strip()
    if not term:
        print("No input provided.")
        t.sleep(1)
        clear_screen()
        main_menu(library)
        return

    term_l = term.lower()
    matches = [book for book in library if any(term_l in str(v).lower() for v in book.values())]

    if not matches:
        print(f"{term} is not in the library, make sure it is spelled correctly next time. ")
        t.sleep(2)
        clear_screen()
        main_menu(library)
        return

    if len(matches) == 1:
        removed = matches[0]
        library.remove(removed)
        save_library(library)
        print(f"Removed: {removed}")
        t.sleep(2)
        clear_screen()
        main_menu(library)
        return

    # multiple matches: show numbered list
    print("Multiple matches found:")
    for idx, book in enumerate(matches, 1):
        print(f"{idx}:", end=" ")
        for k, v in book.items():
            print(f"{k}:{v}", end=" ")
        print()

    choice = input("Enter the number of the item to remove (or 'all' to remove all): ").strip().lower()
    if choice == 'all':
        for b in matches:
            library.remove(b)
        save_library(library)
        print(f"Removed {len(matches)} items.")
        t.sleep(2)
        clear_screen()
        main_menu(library)
        return

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(matches):
            library.remove(matches[idx])
            save_library(library)
            print("Item removed.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

    t.sleep(2)
    clear_screen()
    main_menu(library)

#define a function that allows for you to search the library
def search(library):
    term = input("What do you want to search for in the library? ").strip()
    if not term:
        print("No input provided.")
        t.sleep(1)
        clear_screen()
        main_menu(library)
        return

    term_l = term.lower()
    results = [book for book in library if any(term_l in str(v).lower() for v in book.values())]

    if results:
        for book in results:
            for k, v in book.items():
                print(f"{k}:{v}", end=" ")
            print()
    else:
        print(term, " is not in the library")

    input("\nPress enter to return to the main menu. ")
    clear_screen()
    main_menu(library)

#define a function that exits the program
def exitp():
    print("Okay! See you soon.")

    t.sleep(2)
    print("\033c", end="")
    quit()

main_menu(library)