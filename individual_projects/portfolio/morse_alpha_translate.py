#WG_CP2 morse code translator
#import time as t and random as r
import time as t
import graphics
#a tuple of all the alphabet letters
alpha_code = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#a tuple of all the morse code letters
morse_code = ("._", "_...", "_._.", "_..", ".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".___.","__._","._.","...","_",".._","..._",".___","_.._","_.__","__..")
#define morse code to alphabet
def morse_alpha():
    word = []
    
    character = original()
    characters = character.split(" ")
    if all(c in morse_code for c in characters):
        for x in range(len(characters)):
            word.append(alpha_code[morse_code.index(characters[x])])
        graphics.show(f"{''.join(word)} is {character} in english")
    else:
        graphics.show("That is not morse code please try again, or it is not something that codes for a letter.")
    t.sleep(8)

#define the original function to get the thing they want to translate
def original():
    translate = graphics.inputs("What do you want to translate? Put a space in between morse code characters ").strip().upper()
    t.sleep(3)
    return translate

#define the alphabet to code
def alpha_morse():
    word = original()
    characters = list(word)
    morse_values = []
    valid = True
    for char in characters:
        if char in alpha_code:
            index = alpha_code.index(char)
            morse_values.append(morse_code[index])
        elif char == ' ':
            morse_values.append(' ') # Add space for word separation
        else:
            valid = False
            break
    if valid:
        morse_string = ' '.join(morse_values)
        graphics.show(f"{morse_string} is {word} in morse code")
    else:
        graphics.show("Invalid characters in graphics.inputs. Only letters and spaces allowed.")
    t.sleep(8)

#define a main menu function
def menu():
#use match to let them check if they choose to enter the morse code translator
    while True:
        action = graphics.inputs("Do you want to translate something into morse code? press 1 \nDo you want to translate something into english from morse code? press 2\nOr exit. press 3\n")
        match action:
            case "1":
        
                alpha_morse()
            case "2":
        
                morse_alpha()
            case "3":
        
                exit()
            case _:
                graphics.show("graphics.inputs is not an option")
                t.sleep(3)
        
                continue
menu()