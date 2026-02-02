#WG_CP2 Reading a file 

try:
    with open("Notes/read_file.txt", "r") as file:
        for line in file:
            print(f"Hello {line.strip()}")
        
except:
    print("That file can't be found.")

else:
    print("Code ends")