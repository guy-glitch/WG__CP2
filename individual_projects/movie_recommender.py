#WG_CP2 Movie Recommender 
#import needed modules
import csv
import time as t
# main menu function
def main():
    while True:
        #give them there options search/get recommendations print full movie list or exit
        print("\nTo see full list of offered movies press 1. then enter\n\nTo get recommendations for movies press 2 then enter\n\nTo exit press 3 then enter")
        action = input()
        match action:
                case "1":
                    clear_screen()
                    print_list(cvs_read())
                case "2":
                    clear_screen()
                    updated_list = get_recommendations(cvs_read())
                    clear_screen()
                    if updated_list and len(updated_list) > 0:
                        print("Here are the movies that match your criteria:")
                        print_list(updated_list)
                    else:
                        print("No movies found matching your criteria.")
                case "3":
                    clear_screen()
                    exit()
                case _:
                    print("Input is not an option")
                    t.sleep(3)
                    clear_screen()
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
                rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
    #except file not fpound print there was an error the file can't be found
    except:
         print("For some reason no list of movies is found, please close the program and try again")
    #return the data list
    return rows
#function that goes thorugh and checks every value in a dictionary for a match with that is a parameter the list is also a parameter along with the key it belongs to do this for every option for values that they could search for
def search(list, value, key):
    #a for loop that goes through and checks each index value for a certain value in the inputed keys
    result = []
    for i in list:
        
        if value in i[key]:
            result.append(i)
    return result
#a function that gets what they are searching for after getting how many values they are searching for, and calls each parser function consecutivly inputting them into each other
def get_recommendations(list):
    print("How many things are you searching for? This can only be one genre, one actor, one director, and one rating, or max amount of time, and you can only search for one of each of those things. For example you can search for one genre and one actor but not two genres or two actors.")
    num = input()
    try:
        num = int(num)
    except:
        print("Input is not an option")
        t.sleep(3)
        clear_screen()
        return get_recommendations(list)
    
    list = narrow_down(list, num)
    return list
#a function that clears the screen
def clear_screen():
    print("\033c", end="")
#a function to print list prettly with good spacing
def print_list(list):
    for i in list:
        print(f"Title: {i['Title']}\n\nGenre: {i['Genre']}\n\nNotable Actors: {i['Notable Actors']}\n\nDirector: {i['Director']}\n\nRating: {i['Rating']}\n\n")
#a function that checks the current list of already filtred movies and filters again
def narrow_down(list, times):
    while times > 0:
        print("What are you searching for? Genre press 1, Actor press 2, Director press 3, Maximum time in Minutes press 4, or Rating press 5?")
        search_for = input()
        match search_for:
            case "1":
                print("What genre are you looking for?")
                genre = input().title()
                list = search(list, genre, "Genre")
                times -= 1
            case "2":
                print("What actor are you looking for?")
                actor = input().title()
                list = search(list, actor, "Notable Actors")
                times -= 1
            case "3":
                print("What director are you looking for?")
                director = input().title()
                list = search(list, director, "Director")
                times -= 1
            case "4":
                print("What is the maximum time in minutes you want the movie to be?")
                max_time = input()
                try:
                    max_time = int(max_time)
                except:
                    print("Input is not an option")
                    t.sleep(3)
                    clear_screen()
                    continue
                for i in list:
                    if int(i["Length (min)"])>int(max_time):
                        list.remove(i)
                times -= 1
            case 5:
                print("What rating are you looking for?")
                rating = input().title()
                list = search(list, rating, "Rating")
                times -= 1
            case _:
                print("Input is not an option")
                t.sleep(3)
                clear_screen()
                continue
    return list
#call the main menu funciton to start
print("Welcome to the movie recommender.")
main()