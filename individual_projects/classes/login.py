import time as t
import csv

#A function that takes in a pet and sees if it is already saved in an account if so it saves it to the account that already exists if not it creates a new account with the create account function and saves the pet to that account
def save_pet(pet):
    with open("individual_projects//classes//users.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        username = None
        for row in reader:
            if row and row[1] == str(pet.num):
                username = row[0]
                break
    if username:
        print("Pet already saved to account!")
    else:
        create_account(pet)

#login function that takes in the username and uses the exist function to check if that username exists in the users csv then gets the pet number from the csv for that username and sets pet to the pet with that number in the pet status csv
def login():
    username = input("Please enter your username: ").strip()
    if exists("individual_projects//classes//users.csv", username):
        with open("individual_projects//classes//users.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    pet_num = row[1]
                    break
        with open("individual_projects//classes//pet_status.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row and row.get("number") == pet_num:
                    from pet_control import Pet
                    pet = Pet(
                        int(row["number"]),
                        row["name"],
                        row["species"],
                        int(row["age"]),
                        float(row["health"]),
                        float(row["hunger"]),
                        float(row["happiness"]),
                        float(row["energy"]),
                        int(row.get("time", 0)),
                        int(row.get("level", 1)),
                        row.get("skills", "").split(",") if row.get("skills") else []
                    )
                    break
        return pet
    else:
        print("Username not found. Please try again.")
        return login()

#A function that takes a new username and adds it to the users csv along with their pets number.
def create_account(pet):
    username = input("Please input the username you would like to use: ").strip()
    if exists("individual_projects//classes//users.csv", username):
        print("That username is already taken. Please try again.")
        return create_account(pet)

    # Guarantee file exists and has header row
    users_path = "individual_projects//classes//users.csv"
    try:
        with open(users_path, mode="r", newline="") as f:
            content = f.read()
    except FileNotFoundError:
        with open(users_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "pet_num"])

    # Append the account row on a new line
    with open(users_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, pet.num])

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