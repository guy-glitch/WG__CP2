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
    # Read existing content (if any) and remove previous metadata lines
    try:
        with open(path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Remove any previous metadata lines that start with the marker
    cleaned = [l for l in lines if not l.strip().startswith("This was updated")]

    # Ensure the new content is added as its own line
    cleaned.append(f"\n{adding}")

    # Compute word count excluding metadata lines
    wc = 0
    for line in cleaned:
        wc += len(line.split())

    # Append updated metadata line
    cleaned.append(f"\nThis was updated {current_time()}, and had the word count {wc}\n")

    # Write everything back (overwriting) so previous metadata is removed
    with open(path, "w") as file:
        file.writelines(cleaned)
    
#A function that reads through the entire file and loops through the lines adding them to a variable then prints it
def read(path):
    with open(path, "r") as file:
        for line in file:
            print(line, end="")

#A function that reads through the file and increases a variable by one printing it to give them the word count
def word_count(path):
    count = 0
    with open(path, "r") as file:
        for line in file:
            if line.strip().startswith("This was updated"):
                continue
            count += len(line.split())
    return count
