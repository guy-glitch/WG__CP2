#decorator fiuncton WG_CP2

def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator
def add():
    print(1+1)

add()