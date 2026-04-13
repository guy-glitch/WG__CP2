import random
import time as t
import os
from helper import *
import graphics


def spin_grid():
    symbols = ['🍒', '🥀', '😂', '🍎', '⭐']
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]



def inputgrid(grid):
    graphics.show("*************")
    for row in grid:
        graphics.show("  ", " | ".join(row))
    graphics.show("*************")



def get_payout(grid, bet):
    payout = 0

    for row in grid:
        if row[0] == row[1] == row[2]:
            payout += symbol_multiplier(row[0]) * bet

    if grid[0][0] == grid[1][1] == grid[2][2]:
        payout += symbol_multiplier(grid[0][0]) * bet
    if grid[0][2] == grid[1][1] == grid[2][0]:
        payout += symbol_multiplier(grid[0][2]) * bet

    return payout



def symbol_multiplier(symbol):
    if symbol == '🍒':
        return 3
    elif symbol == '🥀':
        return 4
    elif symbol == '😂':
        return 5
    elif symbol == '🍎':
        return 10
    elif symbol == '⭐':
        return 20
    return 0



def not_main():
    money = 100
    graphics.show("   Welcome to slots!")
    graphics.show("   Symbols: 🍒 🥀 😂 🍎 ⭐")

    while money > 0:
        graphics.show(f"\nCurrent money: ${money}")
        
        bet = graphics.inputs("Place your bet amount: $")
        
        if not bet.isdigit():
            graphics.show("Please enter a valid input.")
            continue

        bet = int(bet)

        if bet > money:
            graphics.show("You don't have that much money.")
            continue
        elif bet <= 0:
            graphics.show("Bet must be greater than 0.")
            continue

        money -= bet
        graphics.show("\nSpinning...\n")
        t.sleep(1)
        grid = spin_grid()
        graphics.show_grid(grid)

        payout = get_payout(grid, bet)
        t.sleep(1)
        if payout > 0:
            graphics.show(f"You won ${payout}!")
            money += payout
            play_again = graphics.inputs("Would you like to continue spinning? y/n\n").capitalize()
             
            if play_again != 'Y':
                quit = graphics.inputs("Would you like to play another game of slots? [this will reset your money to $100] Y/N:\n").strip().capitalize()
                if quit == "Y":
                    # clear screen here
                     
                    continue
                else:   
                    return int(money)
        else:
             
            graphics.show("You lost.")
            play_again = graphics.inputs("Do you want to spin again? (Y/N)\n").upper()
            if play_again != 'Y':
                quit = graphics.inputs("Would you like to continue playing? Y/N:\n").strip().capitalize()
                if quit == "Y":
                    # clear screen here
                     
                    continue
                else:
                    return int(money)
        if money == 0:
            graphics.show("\nNo more money!")
            return int(money)        

        play_again = graphics.inputs("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break
        else:
            # clear screen here
             
            return int(money)
    graphics.show(f"Game over!")



def slots_main():
    while True:
        money = not_main()
        choice = graphics.inputs("Do you want to play again? Y/N:\n").upper()
        if choice != "Y":
            return int(money)
             
        else:
            continue            