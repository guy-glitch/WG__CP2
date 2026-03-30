#The grade for each student grade managment]
import json
from fromatting import *
#A class for the gradebook
class Gradebook:
    
    #__init__ self students set students to an empty list
    def __init__(self, students = []):
        self.students = students
    
    #Add a student method take in the name, student ID
    def add_student(self, name, student_id):
        #create new student using the student class Method
        new_student = Student(name, student_id)
        #add the student to the students list
        self.students.append(new_student)
    
    #A method that allows for you to type in a student ID and change their grade
    def set_student_grade(self, student_id, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.set_grade(grade)
                return
        print("Student not found.")
    
    #search take in a student ID and display the student Method
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Name: {student.name}, Grade: {student.grade}, Letter Grade: {return_letter(student.grade)}")
                return
        print("Student not found.")
    
    #a method that loads the previous gradebook from a json file and a method that saves the current gradebook to the json
    def load_gradebook(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = [Student(**student) for student in data]
        except FileNotFoundError:
            print("Gradebook file not found. Starting with an empty gradebook.")
    
    def save_gradebook(self, filename):
        with open(filename, 'w') as file:
            json.dump([student.__dict__ for student in self.students], file, indent=4)
    
    #Display all of their students and the grade they have along with the avergage grade. Method
    def display_all_students(self):
        if not self.students:
            print("No students in the gradebook.")
            return
        total_grade = 0
        for student in self.students:
            print(f"Name: {student.name}, Grade: {student.grade}, Letter Grade: {return_letter(student.grade)}")
            total_grade += student.grade
        average_grade = total_grade/len(self.students)
        print(f"Average Grade: {average_grade}")

#A class for each student
class Student:
    #initilize self student ID & student name
    def __init__(self, name, student_id, grade = 0):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    #A function that sets a grade for that student
    def set_grade(self, grade):
        self.grade = grade
