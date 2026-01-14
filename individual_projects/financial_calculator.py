#WG_CP3 financial calculator 1st
#import time
import time as t
#clear screen inside of all of the funcitons 
#how to clear the screen
print("\033c", end="")

#def a function that prints out the options and asks them what calculator they want to use 
def main_menu():
    print("Compound Interest Calculator 1 \nBudget Allocator 3  \nSale Price Calculator 3 \n Tip Calculator 4 \nHow long to achieve a savings goal 5")

    type = round(float(input("Press the number that is alligned with the calculator you want to use then press enter")), 3)
    print("\033c", end="")
    if type == 1:
        comp_intrest_calc()
    elif type == 3:
        budget_allocator()
    elif type == 3:
        sale_price()
    elif type == 4:
        tip_calc()
    elif type == 5:
        savings_goal()
    else:
        main_menu()

#define a function that takes in there bank balance and the intrest rate, along with how many months they want to calculate
def comp_intrest_calc():
    balance = round(float(input("What is your bank balance?")), 3)
    rate = (int(input("What is the monthly intrest rate?"))/100)
    time = int(input("How many months do you want to calculate the bank balance ahead of?"))
    for i in range(0, time):
        balance = round(balance + (balance * rate), 3)
        print(f"After {i+1} month(s) your balance is {balance}")
        t.sleep(10)
        print("\033c", end="")
    main_menu()
#define a function that takes there monthly income in and what percentage of the budget they want ot allocate to everything with an inner funciton that takes in the percentages and checks if they add up to 100 if they do find the values that get allocated to everything
def budget_allocator():
    income = float(input("What is your monthly income?"))
    categories = {"Mortgage":0,"Transportation":0,"Groceries":0,"Utilities":0,"Savings":0}

    values = {"Mortgage":0,"Transportation":0,"Groceries":0,"Utilities":0,"Savings":0}
    
    categories["Mortgage"] = (round(float(input("What percentage of your income do you want to allocate to Mortgage? please input only a number.")), 3)/100)
    
    categories["Transportation"] = (round(float(input("What percentage of your income do you want to allocate to Transportation? please input only a number.")), 3)/100)
    
    categories["Groceries"] = (round(float(input("What percentage of your income do you want to allocate to Groceries? please input only a number.")), 3)/100)
    
    categories["Utilities"] = (round(float(input("What percentage of your income do you want to allocate to Utilities? please input only a number.")), 3)/100)
    
    categories["Savings"] = (round(float(input("What percentage of your income do you want to allocate to Savings? please input only a number.")), 3)/100)
    
    if categories["Mortgage"] +  categories["Transportation"] + categories["Groceries"] + categories["Utilities"] + categories["Savings"] == 1.0:
        values["Mortgage"] = income * categories["Mortgage"]
        values["Transportation"] = income * categories["Transportation"]
        values["Groceries"] = income * categories["Groceries"]
        values["Utilities"] = income * categories["Utilities"]
        values["Savings"] = income * categories["Savings"]
        print("\033c", end="")
        print(f"You will have {values["Mortgage"]} allocated to your mortgage \n You will have {values["Transportation"]} allocated to your Transportation \n You will have {values["Groceries"]} allocated to your Groceries \n You will have {values["Savings"]} allocated to your Savings \n")
        t.sleep(15)
        print("\033c", end="")
        main_menu()
    else:
        print("\033c", end="")
        budget_allocator()
#define a funciton that takes in the price of the item and the discount plus an inner function that allows for extra coupons
def sale_price():
    original = round(float(input("What is the original price of the item")), 3)
    discount = (round(float(input("What is the discount")), 3)/100)
    final = 0
    def coupon(final):
        coupon = round(float(input("How many dollars off is the coupons?")), 3)
        final = final - coupon
        return final
    final = original - (original * discount)
    if_coupon = input("Is there a special extra coupon that you can apply? y/n").strip().lower()
    if if_coupon == "y":
        print(f"${coupon(final)} is the new price after the discount and coupon")
    else:
        print(f"${final} is the new price after the discount")
    t.sleep(10)
    print("\033c", end="")
    main_menu()
#define a funciton that takes in the price of the meal and the percentage they want to tip and gives them how much they should pay in total 
def tip_calc():
    price = round(float(input("What is the price of the meal")), 3)
    tip = (float(input("What percentage do you want to tip?"))/100)
    total = price + (price * tip)
    print(f"You should pay ${total}")
    t.sleep(5)
    print("\033c", end="")
    main_menu()
#define a function that takes in there current savings, the amount they want they want to reach, and the monthly deposit they are going to make, then tells them how many months it will take to reach that goal
def savings_goal():
    current_savings = round(float(input("What is your current savings?")), 3)
    goal = round(float(input("What is your savings goal?")), 3)
    monthly_deposit = round(float(input("How much are you going to deposit each month?")), 3)
    months = 0
    while current_savings < goal:
        current_savings = current_savings + monthly_deposit
        months = months + 1
    print(f"It will take you {months} month(s) to reach your savings goal of ${goal}")
    t.sleep(10)
    print("\033c", end="")
    main_menu()
#call main menu
main_menu()