import time as t
import csv

#A function that takes in a pet and sees if it is already saved in an account if so it saves it to the account that already exists if not it creates a new account with the create account function and saves the pet to that account
def save_pet(pet):
    with open("individual_projects//classes//users.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        username = None
        for row in reader:
            if row and row[1] == str(pet["number"]):
                username = row[0]
                break
    if username:
        print("Pet already saved to account!")
    else:
        create_account(pet)

#login function that takes in the username and uses the exist function to check if that username exists in the users csv then gets the pet number from the csv for that username and sets pet to the pet with that number in the pet status csv
def login():
    username = input("Please enter your username: ").strip()
    if exists("users.csv", username):
        with open("users.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    pet_num = row[1]
                    break
        with open("individual_projects//classes//pet_status.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file, fieldnames=["number", "name","type","age","health","hunger","happiness","energy"])
            for row in reader:
                if row and row["number"] == pet_num:
                    pet = row
                    pet["number"] = int(pet["number"])
                    pet["age"] = int(pet["age"])
                    pet["health"] = float(pet["health"])
                    pet["hunger"] = float(pet["hunger"])
                    pet["happiness"] = float(pet["happiness"])
                    pet["energy"] = float(pet["energy"])
                    break
        return pet
    else:
        print("Username not found. Please try again.")
        return login()

#A function that takes a new username and adds it to the users csv along with their pets number.
def create_account(pet):
    username = input("Please input the username you would like to use: ").strip()
    if exists("users.csv", username):
        print("That username is already taken. Please try again.")
        return create_account(pet)
    else:
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, pet["number"]])
        print("Account created successfully!")
        return pet
#define a function that checks if a username exists in a csv (first column)
def exists(location, search):
    try:
        with open(location, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # skip empty lines
                if row and row[0] == search:
                    return True
    except FileNotFoundError:
        print("file does not exist.")
    except Exception:
        # fallback for unexpected errors
        print("error reading file")
    return False

#A function to clear the screen
def clear_screen():
    t.sleep(3)
    print("\033c", end="")