#WG_CP2 all helper functions
#import datetime and zoneinfo and time
import time
from datetime import datetime
from zoneinfo import ZoneInfo
#function that uses the clear screen, and also waits a certain amount of time between being called and clearing the screen
def clear_screen():
    time.sleep(3)
    print("\033c", end="")
# Get the current time in Utah's timezone and have it as a function 
def current_time():
    # Return current time in Utah (Mountain Time) with timezone name.
    now = datetime.now(ZoneInfo("America/Denver"))
    return now.strftime("%m-%d-%Y %H:%M:%S %Z")
