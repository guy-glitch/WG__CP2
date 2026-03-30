#Inheritance is a class where the relation ship is a
#parent class
class Vehicle:
     def __init__(self, model, brand):
         self.brand = brand
         self.model = model
     def move(self):
         print("Move! ")

 #child class
class Car(Vehicle):
     pass

class Boat(Vehicle):
     def move(self):
         print("Sail")

class Plane(Vehicle):
     def move(self):
         print("Fly! ")
car = Car("Ford", "Mustang")

print(car.brand)
print(car.model)
car.move()

boat = Boat("Ibiza", "Touring 20")
print(boat.brand)
print(boat.model)
boat.move()

plane = Plane("747", "Boeing")
plane.move()
print(plane.brand)
print(plane.model)

 #Aggregation
class Library:
     def __init__(self, name, catalog = []):
         self.name = name
         self.catalog = catalog
     def add_book(self, book):
         self.catalog.append(book)
 
     def remove_book(self, book):
         if book in self.catalog:
             self.catalog.pop(book)
         else:
             print("That book does not exist. ")

     def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
   def __init__(self, title, author):
       self.title = title.title()
       self.author = author

   def __str__(self):
        return f"Title: {self.title} by {self.author}"
    
lib = Library("Provo Library")
lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Words of Raidiance", "Brandon Sanderson"))
lib.add_book(Book("Yumi and the Nightmare Painter", "Brandon Sanderson"))

lib.view_catalog()