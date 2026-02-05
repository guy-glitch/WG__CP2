#WG_CP2 Movie Recommender 
#import needed modules
import csv
import time as t
# main menu function
def main():
    while True:
        #give them there options search/get recommendations print full movie list or exit
        print("\nTo see full list of offered movies press 1. then enter\n To get recommendations for movies press 2 then enter\n To exit press 3 then enter")
        action = input()
        match action:
                case "1":
                    print("\033c", end="")
                    ()
                case "2":
                    print("\033c", end="")
                    ()
                case "3":
                    print("\033c", end="")
                    exit()
                case _:
                    print("Input is not an option")
                    t.sleep(3)
                    print("\033c", end="")
                    continue
#function that reads the csv file and stores it in a list of dictionaries
def cvs_read():
    #use the filename as a parameter
    #try open the file with mode r newline as "" encoing utf-8 as file
    try:
        with open("individual_projects/Movies list.csv", mode="r") as file:
            content = csv.reader(file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]: line[0], headers[1]: line[1]})
    #except file not fpound print there was an error the file can't be found
    except:
         print("For some reason no list of movies is found close the program and try again")
    #return the data list
    return rows
#function that goes thorugh and checks every value in a dictionary for a match with that is a parameter the list is also a parameter along with the key it belongs to
    #a for loop that goes through and checks each index value for a certain value in the inputed keys
#a function that gets what they are searching for after getting how many values they are searching for, and calls each parser function consecutivly inputting them into each other
#a function that clears the screen
#a function to print list prettly with good spacing
#a function that checks a dictionary and searches through it adding the key of the values that meet the requirnments 
    