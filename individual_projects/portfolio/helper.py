#Clear screen function
import time as t

def clear_screen():
    t.sleep(2)
    print("\033c", end="")