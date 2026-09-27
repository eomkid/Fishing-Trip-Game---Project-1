"""Program: Fishing Trip
Author: Brandon Barrett
Description: This is a simple game about catch fish, selling what you caught to buy bait, and continuing to catch more fish.
Date: August 27, 2026
"""
from random import choice
from random import randint
"""Randint: Imported for the purpose of having randomness to the hooking of a fish, allow the action to fail."""
"""Choice: This is will be use to pick a random fish to for the user to catch"""
print("Welcome angler, let's get to fishing.\n")

starting_money = 100
fish_stored = []
bait = 0
fish_count_to_sell = 1

player_money = starting_money
fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                     "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

play_state = input("Would you like to go fishing (Y/N)?").upper().strip()
while play_state != "Y" and play_state != "N":
    play_state = input(
        "\nPlease only used Y or N as your response\nWould you like to go fishing (Y/N)?").upper().strip()

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

while play_state != "N":
    print("--------------------")
    print("""   Fishing Trip
1: Fish!!!
2: Sell Fish
3: Check Money
4: Buy Bait
5: See Your Haul
6: Call it A Day""")
    print("--------------------\n")

    try:
        menu_choice = int(
            input("What would you like to do, pick a number 1 - 6:\n"))
    except ValueError:
        print("Please enter a positive whole number 1 - 6. \n")
        continue

    if menu_choice == 6:
        play_state = "N"
        break

    if menu_choice == 1:
        catch_or_not = randint(0, 1)
        if catch_or_not == 0 and bait > 0:
            bait -= 1
            print("Dang that fish was such a monster it snapped the line and stole the bait.\n What a waste of good bait.")

        elif catch_or_not == 0 and bait == 0:
            print("Don't ask me how... \nBut the Goldfish broke the line and got away \nYou might wanna get a better fishing line just saying.")

        elif catch_or_not == 1 and bait > 0:
            bait -= 1
            random_fish_pull = choice(list(fishes_and_prices))
            fish_price_check = fishes_and_prices[random_fish_pull]
            fish_stored.append(random_fish_pull)
            print(
                f"Nice nice, you caught a {random_fish_pull} I would say you could sell it for about ${fish_price_check}")
            sell_now = input(
                f"Would you like to sell that {random_fish_pull} now(Y/N)?").upper().strip()

            if sell_now == "Y":
                player_money += fish_price_check
                print("Pleasure doing business with you")
                fish_stored.remove(random_fish_pull)
            elif sell_now == "N":
                print(
                    f"Keep your {random_fish_pull} I didn't want to buy it anyway.")
            else:
                print(
                    f"Ill just take that as a no \nKeep your {random_fish_pull} I didn't want to buy it anyway.")

        elif catch_or_not == 1 and bait == 0:
            random_fish_pull = "Goldfish"
            fish_price_check = fishes_and_prices[random_fish_pull]
            fish_stored.append(random_fish_pull)
            print()
            print(
                f"You caught a {random_fish_pull} :| \nIt's not worth much only ${fish_price_check}\n")
            sell_now = input(
                f"Would you like to sell that {random_fish_pull} now(Y/N)?").upper().strip()

            if sell_now == "Y":
                player_money += fish_price_check
                print("Pleasure doing business with you")
                fish_stored.remove(random_fish_pull)
            elif sell_now == "N":
                print(
                    f"Keep your {random_fish_pull} I didn't want to buy it anyway.")
            else:
                print(
                    f"Ill just take that as a no \nKeep your {random_fish_pull} I didn't want to buy it anyway.")

    if menu_choice == 2:
        if fish_stored == []:
            print("You have nothing to sell come back when you actually catch something.")
        else:
            print("Looking to sell?\n")
            for fish in fish_stored:
                print(fish)
            fish_to_sell = input(
                "Please input a single type of fish you would like to sell:\n")
            if fish_to_sell not in fishes_and_prices or fish_stored.count(fish_to_sell) == 0:
                print("You don't have that fish.")
            else:
                fish_price_check = fishes_and_prices[fish_to_sell]
                if fish_stored.count(fish_to_sell) > 1:
                    fish_count_to_sell = int(
                        input("How many are we selling today?\n"))
                for count in range(fish_count_to_sell):
                    fish_stored.remove(fish_to_sell)
                    player_money += fish_price_check
                print("Thank you for your business")

    if menu_choice == 3:
        print(f"\nYou have ${player_money}")
        print("...")
        print("So are you willing to share?\n")

    if menu_choice == 4:
        print("Entering 0 if you no longer wish to go through with your bait purchase \n")
        print(f"You currently have {bait} bait.")
        bait_purchase_amount = int(input(
            "Please enter the amount of bait ($25 per) you would like to purchase (Whole numbers only).\n"))
        purchase_cost = bait_purchase_amount * 25
        if bait_purchase_amount == 0:
            continue
        while purchase_cost > player_money and bait_purchase_amount != 0:
            print(
                f"You don't have enough money for that purchase. \nYou only have ${player_money} and that amount of bait would cost ${purchase_cost}\n")
            bait_purchase_amount = int(
                input("Please enter a smaller amount of bait ($25) to purchase.\n"))
            purchase_cost = bait_purchase_amount * 25
        player_money -= purchase_cost
        bait += bait_purchase_amount
        print(
            f"You bought {bait_purchase_amount} bait. \nYou have ${player_money} left.\n")

    if menu_choice == 5 and fish_stored != []:
        print("You have might haul here \nSo far you've caught:")
        for fish in fish_stored:
            print(fish)
    elif menu_choice == 5 and fish_stored == []:
        print("I've been looking for like 5 whole nanoseconds and I dont see anything in here\n"
              "Maybe try catching something before you try looking at your haul.")

print("""Calling it a day already
Well hope you had fun but lets see what you got from today.""")
if fish_stored == []:
    print(f"Oh you didn't catch anything :( \nBad RNG I guess")
elif fish_stored != []:
    print("Nicely done I respect the haul enjoy your dinner :)")
    for fish in fish_stored:
        print(fish)
elif player_money <= 24 and bait != 0:
    print("Maybe I should've made bait cheaper")
    print(
        f"Look at the bright side you had {bait} bait leftover that has to count for something.")
elif player_money >= 10000:
    print(f"${player_money} Are you ok?")
elif 1000 > player_money > 100:
    print(f"Pure profit :) \nWalking away with ${player_money}")
else:
    print("ByeBye Thank yous for playing :)")
