#WG_CP2 The main menu
#import what is needed
import time as t
from grade_manager import *
from fromatting import *
gradebook = Gradebook()

#Main menu function defined
def main_menu():

    #infinite loop
    while True:
        print("Do you want to \n1 add a student\n2 set a students grade\n3 veiw student records\n4 veiw the overall class summary\n5 save gradebook\n6 load gradebook\n7 exit")
        action = input("Please enter your choice: \n")

        #Use match case to
        match action:

            case "1":
                name = input("Enter the student's name: ")
                student_id = input("Enter the student's ID: ")
                print("Adding student... Student grade will be set to 0 by default.")
                read_wipe()
                gradebook.add_student(name, student_id)
                t.sleep(1)
                wipe()

            case "2":
                student_id = input("Enter the student's ID: ")
                grade = int(input("Enter the student's grade: "))
                gradebook.set_student_grade(student_id, grade)
                t.sleep(1)
                read_wipe()

            case "3":
                student_id = input("Enter the student's ID: ")
                gradebook.search_student(student_id)
                t.sleep(1)
                wipe()

            case "4":
                gradebook.display_all_students()
                read_wipe()

            case "5":
                gradebook.save_gradebook("individual_projects//simple_grade.py//gradebook.json")
                print("Gradebook saved.")
                t.sleep(1)
                wipe()

            case "6":
                gradebook.load_gradebook("individual_projects//simple_grade.py//gradebook.json")
                print("Gradebook loaded.")
                t.sleep(1)
                wipe()

            case "7":
                print("Exiting the program.")
                wipe()
                exit()

            case _:
                print("Invalid choice. Please try again.")
                continue
        #do they want to add a student
        #set a students grade
        #veiw student records
        #veiw the overall class summary
        #exit

main_menu()