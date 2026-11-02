"""Program: Fishing Trip
Author: Brandon Barrett
Description: This is a simple game about catch fish, selling what you caught to buy bait, and continuing to catch more fish.
Date: November 1, 2026
"""
from menu import MainMenu
import player


def main():
    print("Welcome angler, let's get to fishing.\n")
    play_state = input("Would you like to go fishing (Y/N)?").upper().strip()
    if play_state == "Y":
        print()
        print("""You ready to cast your line!
Good let me give you the run down
The game is very simple you Fish!!!, and if you get lucky
You catch whatever you hook, then you have the option to sell it now or later
Bare in mind though if you dont sell your fish before you call it a day
Back in the pond they go.
Good luck have fun
Also I suggest using bait""")
        player.player1.load()
    menu = MainMenu()
    menu.menu_choice(play_state)


if __name__ == "__main__":
    main()
