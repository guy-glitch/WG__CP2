#WG_CP2 all helper functions
#import datetime and zoneinfo and time
import time
from datetime import datetime

#function that uses the clear screen, and also waits a certain amount of time between being called and clearing the screen
def clear_screen():
    time.sleep(3)
    print("\033c", end="")
# Get the current time in Utah's timezone and have it as a function 
def current_time():
    # Return current time in Utah (Mountain Time) with timezone name.
    current_time = datetime.now()

    year = current_time.year
    month = current_time.month
    day = current_time.day

    date = f"{year}-{month}-{day}"

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    time = f"{hour}:{minute}:{second}"
   
    date_time = f"Last updated: {date} {time}"

   

    return date_time

