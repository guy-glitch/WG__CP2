
#import time and csv, along with clear screen from login and random
import random as r
import time as t
import csv
from login import clear_screen
types = ["dog","fish","cat","lizard","spider"]

#class Pet
class Pet:
    def __init__(self, num, name, species, age, health, hunger, happiness, energy, time=0, level=1, skills=None):
        self.num = num
        self.name = name
        self.species = species  # renamed from type to species
        self.age = age  # in months
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.time = time  # game time in hours
        self.level = level
        self.skills = skills if skills else []  # list of learned skills

    def feed(self):
        foods = {
            "dog": {
                "1": {"name": "Dog food", "hunger": 10, "happiness": -10, "energy": 10, "health": 0},
                "2": {"name": "Steak", "hunger": 20, "happiness": 20, "energy": 2, "health": 0},
                "3": {"name": "Ice cream", "hunger": -5, "happiness": 5, "energy": 5, "health": -5}
            },
            "cat": {
                "1": {"name": "Cat food", "hunger": 30, "happiness": -10, "energy": 10, "health": 0},
                "2": {"name": "Fish", "hunger": 15, "happiness": 15, "energy": 15, "health": 0},
                "3": {"name": "Milk", "hunger": 5, "happiness": 5, "energy": -5, "health": -5}
            },
            "fish": {
                "1": {"name": "Fish flakes", "hunger": 10, "happiness": -10, "energy": 10, "health": 0},
                "2": {"name": "Worms", "hunger": 20, "happiness": 15, "energy": 5, "health": 0},
                "3": {"name": "Bread", "hunger": 20, "happiness": 5, "energy": 5, "health": -7}
            },
            "lizard": {
                "1": {"name": "Crickets", "hunger": 10, "happiness": -10, "energy": 10, "health": 0},
                "2": {"name": "Mealworms", "hunger": 15, "happiness": 20, "energy": 5, "health": 0},
                "3": {"name": "Fruit", "hunger": 10, "happiness": 10, "energy": -5, "health": -5}
            },
            "spider": {
                "1": {"name": "Flies", "hunger": 10, "happiness": -10, "energy": 10, "health": 0},
                "2": {"name": "Moths", "hunger": 20, "happiness": 15, "energy": 5, "health": 0},
                "3": {"name": "Sugar", "hunger": 5, "happiness": 5, "energy": -5, "health": -5}
            }
        }
        
        if self.species in foods:
            print(f"You can feed your {self.species}:")
            for key, food in foods[self.species].items():
                print(f"{key}. {food['name']} (hunger {food['hunger']:+d}, happiness {food['happiness']:+d}, energy {food['energy']:+d}, health {food['health']:+d})")
            choice = input("What would you like to feed your pet? ").strip()
            if choice in foods[self.species]:
                food = foods[self.species][choice]
                self.hunger = max(0, min(100, self.hunger + food['hunger']))
                self.happiness = max(0, min(100, self.happiness + food['happiness']))
                self.energy = max(0, min(100, self.energy + food['energy']))
                self.health = max(0, min(100, self.health + food['health']))
                self.update_health()
                self.time += 1  # advance time
                self.check_level_up()
                print("Status updated!")
                clear_screen()
                save(self)
            else:
                print("That is not an option, please try again.")
                self.feed()
        else:
            print("Unknown species")

    def play(self):
        self.energy = max(0, self.energy - 30)
        self.happiness = min(100, self.happiness + 20)
        self.hunger = max(0, self.hunger - 10)
        self.update_health()
        self.time += 1
        self.check_level_up()
        save(self)

    def sleep(self):
        self.energy = min(100, self.energy + 20)
        self.happiness = min(100, self.happiness + 10)
        self.hunger = max(0, self.hunger - 10)
        self.update_health()
        self.time += 1
        self.check_level_up()
        save(self)

    def update_health(self):
        # Health decreases if stats are low
        penalty = 0
        if self.hunger < 20:
            penalty += 10
        if self.happiness < 20:
            penalty += 10
        if self.energy < 20:
            penalty += 10
        self.health = max(0, min(100, (self.energy + self.happiness + self.hunger) / 3 - penalty))

    def check_level_up(self):
        # Level up every 10 actions or when age increases significantly
        if self.time % 10 == 0 and self.level < 10:
            self.level += 1
            self.learn_skill()

    def learn_skill(self):
        skills = ["Fetch", "Purr", "Swim", "Climb", "Web Spin"]
        if len(self.skills) < self.level:
            new_skill = r.choice(skills)
            if new_skill not in self.skills:
                self.skills.append(new_skill)
                print(f"Your pet learned a new skill: {new_skill}!")

    def display_status(self):
        print(f"Your pet's name is {self.name}, they are a {self.age} month old {self.species} at level {self.level}.")
        print(f"Skills: {', '.join(self.skills) if self.skills else 'None'}")
        print(f"Health: {self.health:.1f}, Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}")
        print(f"Game time: {self.time} hours")
        


#define a function called create_pet that takes in the users input for the name, type, and age of their pet and creates a pet object with those values and the rest being random then saves it to the csv
def create_pet():
    name = input("What would you like to name your pet? ").strip()
    clear_screen()
    species = input("What type of pet would you like? (dog, cat, fish, lizard, spider) ").strip().lower()
    clear_screen()
    age = int(input("How old is your pet in months? ").strip())
    clear_screen()
    energy = r.randint(30,99)
    clear_screen()
    happiness = r.randint(30,99)
    clear_screen()
    hunger = r.randint(30,99)
    clear_screen()
    health = (energy+happiness+hunger)/3
    try:
        with open("individual_projects//classes//pet_status.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            nums = [int(row['number']) for row in reader if row and row.get('number')]
            num = max(nums) + 1 if nums else 1
    except FileNotFoundError:
        num = 1
    pet = Pet(num, name, species, age, health, hunger, happiness, energy)
    save(pet)
    return pet
#A function that save/updates the pet entry in pet_status.csv
def save(pet):
    filename = "individual_projects//classes//pet_status.csv"
    headers = ["name", "species", "age", "health", "hunger", "happiness", "energy", "number", "time", "level", "skills"]
    existing = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            # Only keep actual pet rows (skip empty and filter out the updated ID)
            for row in reader:
                if row and row.get("number") and row.get("number") != str(pet.num):
                    existing.append(row)
    except FileNotFoundError:
        pass

    existing.append({
        "name": pet.name,
        "species": pet.species,
        "age": pet.age,
        "health": pet.health,
        "hunger": pet.hunger,
        "happiness": pet.happiness,
        "energy": pet.energy,
        "number": pet.num,
        "time": pet.time,
        "level": pet.level,
        "skills": ",".join(pet.skills)
    })

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(existing)



