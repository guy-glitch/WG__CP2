
import csv
import hashlib

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
def clear_screen():
    print("\033c", end="")
def hash_pw(item: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(item.encode("utf-8"))
    return sha256.hexdigest()


def user_exists(username: str) -> bool:
    return exists(, username)


def add_user(username: str, hashed: str) -> None:

    with open(USER_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f,
                                fieldnames=["username", "password",
                                            "poker_score", "slots_score",
                                            "blackjack_score"])
        writer.writerow({"username": username,
                         "password": hashed,
                         "poker_score": 0,
                         "slots_score": 0,
                         "blackjack_score": 0})


def create_account():
    # clear screen here
    clear_screen()

    while True:
        name = input("Choose a username: ").strip()

        if not name:
            print("Username cannot be blank.")
            continue

        if user_exists(name):
            print("That username is unavailable.")
            continue

        pw = input("Choose a password (12+ chars, upper, lower, digit, special): ")

        add_user(name, hash_pw(pw))
        print("Account created.")
        break


def parse_user():
    return parse_user_info()


def user_display(users):

    for idx, u in enumerate(users, start=1):
        print(f"{idx}. {u['username']}")


#define a function that is called when the username is admin that allows for accounts to be removed
def admin():

    while True:
        print("To delete an account press 1\nTo exit press 2")
        action = input().strip()

        match action:

            case "1":
                # clear screen here
                clear_screen()
                users = parse_user()
                user_display(users)
                removing = input("Please input the number you want to delete. ").strip()

                if not removing.isdigit():
                    print(f"{removing} is not an option please try again")
                    continue
                idx = int(removing) - 1
                removed = remove(idx)

                if removed:
                    print(f"Removed account: {removed['username']}")

                else:
                    print(f"{removing} is not an option please try again")

            case "2":
                return

            case _:
                print("Invalid selection. Please try again.")

#define a function that edits the account csv removing or adding accounts to the user csv
def add(username, password):

    with open("Notes/sample.csv", 'r+', newline='') as csvfile:
        feildnames = ["username", "password"]
        reader=csv.reader(csvfile)

        for line in reader:
            print(f"{feildnames[0]}, {line[0]} favorite color {line[1]}")
        writer = csv.DictWriter(csvfile, fieldnames=feildnames)
        #writer.writeheader()
        writer.writerow({'username':username, 'password':password})
        



def login(poker_scores,blackjack_scores,slots_scores):
    users = parse_user()
    name = input("What is your username? ").strip()
    pw = input("What is your password? ")
    hashed = hash_pw(pw)

    if name == "admin":

        if hashed == hash_pw("1234"):
            admin()

    for u in users:

        if u["username"] == name and u["password"] == hashed:
            print("Login successful.")
            clear_screen()
            overall_game_menu(name)
            return
    print("Invalid username or password.")