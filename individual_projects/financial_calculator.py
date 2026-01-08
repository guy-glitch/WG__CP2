#WG_CP2 financial calculator 1st
#clear screen inside of all of the funcitons 
#how to clear the screen
print("\033c", end="")

#def a function that prints out the options and asks them what calculator they want to use 
def main_menu():
    print("Compound Interest Calculator 1 \n Budget Allocator 2  \n Sale Price Calculator 3 \n Tip Calculator 4")

    type = int(input("Press the number that is alligned with the calculator you want to use then press enter"))
    print("\033c", end="")
    if type == 1:
        comp_intrest_calc()
    elif type == 2:
        budget_allocator()
    elif type == 3:
        sale_price()
    elif type == 4:
        tip_calc()
    else:
        main_menu()

#define a function that takes in there bank balance and the intrest rate

#define a function that takes there monthly income in and what percentage of the budget they want ot allocate to everything with an inner funciton that takes in the percentages and checks if they add up to 100 if they do find the values that get allocated to everything

#define a funciton that takes in the price of the item and the discount plus an inner function that allows for extra coupons

#define a funciton that takes in the price of the meal and the percentage they want to tip and gives them how much they should pay in total 