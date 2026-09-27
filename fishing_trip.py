"""Program: Fishing Trip
Author: Brandon Barrett
Description: This is a simple game about catch fish, selling what you caught to buy bait, and continuing to catch more fish.
Date: August 27, 2026
"""
from random import choice
from random import randint
"""Imported for the purpose of having randomness to the hooking of a fish, allow the action to fail."""
"""This is will be use to pick a random fish to for the user to catch"""

starting_money = 100

# player_name = input("Welcome to the pond \nWhat do you call yourself?\n")
player_name = "Brandon"

player_money = starting_money
fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                     "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

random_fish_pull = choice(list(fishes_and_prices))
fish_price_check = fishes_and_prices[random_fish_pull]

print(f" You caught a {random_fish_pull} it worth ${fish_price_check}")

fish_caught_today = []
