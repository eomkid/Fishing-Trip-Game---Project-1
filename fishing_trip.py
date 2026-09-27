"""Program: Fishing Trip
Author: Brandon Barrett
Description: This is a simple game about catch fish, selling what you caught to buy bait, and continuing to catch more fish.
Date: August 27, 2026
"""
from random import choice
from random import randint
"""Randint: Imported for the purpose of having randomness to the hooking of a fish, allow the action to fail."""
"""Choice: This is will be use to pick a random fish to for the user to catch"""
print("Welcome angler, let's get to fishing.")

starting_money = 100
# player_name = input("Welcome to the pond \nWhat do you call yourself?\n")
player_name = "Brandon"
fish_stored = []
bait = 0
# If player has no bait they only catch goldfish

player_money = starting_money
fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                     "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

# random_fish_pull = choice(list(fishes_and_prices))
# fish_price_check = fishes_and_prices[random_fish_pull]


# print(f" You caught a {random_fish_pull} it worth ${fish_price_check}")

play_state = input("Would you like to go fishing (Y/N)?")
while play_state.upper() != "Y" and play_state.upper() != "N":
    play_state = input(
        "\nPlease only used Y or N as your response\nWould you like to go fishing (Y/N)?")

while play_state.upper() != "N":
    print("""Your ready to cast your line!
Good let me give you the run down
The game is very simple you Fish!!!, and if you get luck
You catch whatever you hook, then you have the option to sell it now or later
Bare in mind though if you dont sell your fish before you call it a day
Back in the pond they go.
Good luck have fun
Also I suggest using bait""")
    print()
    print("""   Fishing Trip
1: Fish!!!
2: Sell Fish
3: Check Money
4: Buy Bait
5: See Your Haul
6: Call it A Day""")

    play_state = input("Would you like to go fishing (Y/N)?")
