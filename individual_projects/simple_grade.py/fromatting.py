#import time, and json
import time as t, json
#A clear screen instant function
#A clear screen read time funtion
#A function that turns an object into a dictionary then adds it to a json
def dict_transform(object):
    def object_to_dict(obj):
        return json.loads(
            json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
        )
    obj_dict = object_to_dict(object)
    return obj_dict
    
#A function that returns a letter grade based off of the actual grade of the student