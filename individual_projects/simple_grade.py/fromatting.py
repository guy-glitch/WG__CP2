#import time, and json
import time as t, json
#A clear screen instant function
def wipe():
    print("\033c", end="")
#A clear screen read time funtion
def read_wipe():
    input("Press enter to continue....")
    wipe()
#A function that turns an object into a dictionary then adds it to a json
def dict_transform(object):
    def object_to_dict(obj):
        return json.loads(
            json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
        )
    obj_dict = object_to_dict(object)
    return obj_dict
    
#A function that returns a letter grade based off of the actual grade of the student
def return_letter(grade):
    try:
        int(grade)
    except:
        return "grade is not a number"
    if grade >= 94:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >=70:
        return "C"
    elif grade >=60:
        return "D"
    else:
        return "F"