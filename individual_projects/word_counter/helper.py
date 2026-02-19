#WG_CP2 all helper functions
#import datetime and zoneinfo
from zoneinfo import ZoneInfo
from datetime import datetime
#function that clears the screen
#function that uses the clear screen, and also waits a certain amount of time between being called and clearing the screen
# Get the current time in Utah's timezone and have it as a function 
def time():
    utah_tz = ZoneInfo("America/Denver")
    current_time_utah = datetime.now(utah_tz)
    return current_time_utah
