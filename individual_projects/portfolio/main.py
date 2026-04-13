#WG_CP2 Personal portfolio
import graphics,fractal_pattern_generator,slots,morse_alpha_translate,updated_per_library
#Use graphics to create a main function that displays buttons for every option
def main():
    graphics.show("Welcome to my personal portfolio! Click on any project to get more information then click run to run the program.")
    menu = graphics.Menu(["Fractal Pattern Generator","Slots","Personal library","Morse Code Translaotor"])
    while True:
        button = menu.use()
        match button:
            case "Fractal Pattern Generator":
                graphics.show("Creates a fractal using turtle graphics, up to 6 recursions deep. I learned how recursion works. The main challenge was finding an amount of recursions that didn't take 40 minutes but still looked cool.")
                fractal_pattern_generator.main()
            case "Slots":
                graphics.show("A slots game. I learned that emojis can be used in python strings. The main challenge was making the game loop so they didn't have to restart every time.")
                slots.main()
            case "Personal library":
                graphics.show("A library management program. I learned how to save lists and data to csvs files. The main challenge was formatting the csv correctly. ")
                updated_per_library.main()
            case "Morse Code Translaotor":
                graphics.show("A code that translates morse code to english and the other way around. I learned how to use tuples and store data. The biggest challenge was making everything save correctly.")
                morse_alpha_translate.menu()