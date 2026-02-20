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
    time_current= datetime.now()

    year = time_current.year
    month = time_current.month
    day = time_current.day

    date = f"{month}--{day}--{year}"

    hour = time_current.hour
    minute = time_current.minute
    second = time_current.second

    seconds = f"{hour}--{minute}--{second}"

    current_time_utah = f"Time {date} {seconds}"
    return current_time_utah
