import player
import fish as fh
player.player1.load()


class MainMenu:
    def __init__(self):
        self.options = {1: "1: Fish!!!", 2: "2: Sell Fish", 3: "3: Check Money",
                        4: "4: Buy Bait", 5: "5: See Your Haul", 6: "6: Call it A Day"}

    def menu_display(self):
        print("--------------------")
        print("   Fishing Trip   ")
        for options in self.options.values():
            print(options)
        print("--------------------\n")

    def menu_choice(self, play_state: str):
        while play_state.upper() != "N":
            self.menu_display
            try:
                """Error handling for invalid input in main menu"""
                player_choice = int(
                    input("What would you like to do, pick a number 1 - 6:\n"))
            except ValueError:
                print("Please enter a positive whole number 1 - 6. \n")
                continue

            if player_choice == 6:
                player.player1.save()
                play_state = "N"
                print("""Calling it a day already
                        Well hope you had fun but lets see what you got from today.""")
                if not player.player1.fish_stored:
                    print("Oh you didn't catch anything :( \nBad RNG I guess")
                else:
                    print("Nicely done I respect the haul enjoy your dinner :)")
                    for fish in player.player1.fish_stored:
                        print(fish)

                print()

                money = player.player1.money
                bait = player.player1.bait

                if money >= 10000:
                    print(f"${money} Are you ok?")
                elif money <= 24 and bait != 0:
                    print("Maybe I should've made bait cheaper")
                    print(
                        f"Look at the bright side you had {bait} bait leftover that has to count for something.")
                elif 100 < money < 1000:
                    print(f"Pure profit :) \nWalking away with ${money}")
                else:
                    print("ByeBye Thank yous for playing :)")
                break

            if player_choice == 1:
                self.fish()

            if player_choice == 2:
                self.sell_fish()

            if player_choice == 3:
                self.check_player_money()

            if player_choice == 4:
                self.buy_bait()

            if player_choice == 5:
                self.look_at_haul()

    def fish(self):
        fish_caught, fish_price_check = player.player1.fishing_action()
        if fish_caught != "":
            sell_now = input(
                f"Would you like to sell that {fish_caught} now(Y/N)?").upper().strip()
            if sell_now == "Y":
                self.sell_fish(fish_caught)
            elif sell_now == "N":
                print(
                    f"Keep your {fish_caught} I didn't want to buy it anyway.")
            else:
                print(
                    f"Ill just take that as a no \nKeep your {fish_caught} I didn't want to buy it anyway.")
        return fish_caught, fish_price_check

    def sell_fish(self, fish_to_sell=""):
        if fish_to_sell == "":
            fish_to_sell = input("What fish would you like to sell?\n")
        player.player1.add_money(fish_to_sell)
        print(f"Pleasure doing business with you")
        player.player1.fish_stored.remove(fish_to_sell)

    def check_player_money(self):
        player.player1.check_money()

    def buy_bait(self):
        print("Entering 0 if you no longer wish to go through with your bait purchase \n")
        print(f"You currently have {player.player1.bait} bait.")
        bait_purchase_amount = int(input(
            "Please enter the amount of bait ($25 per) you would like to purchase (Whole numbers only).\n"))
        purchase_cost = bait_purchase_amount * 25
        if bait_purchase_amount == 0:
            pass
        while purchase_cost > player.player1.money and bait_purchase_amount != 0:
            print(
                f"You don't have enough money for that purchase. \nYou only have ${player.player1.money} and that amount of bait would cost ${purchase_cost}\n")
            bait_purchase_amount = int(
                input("Please enter a smaller amount of bait ($25) to purchase.\n"))
            purchase_cost = bait_purchase_amount * 25
        player.player1.money -= purchase_cost
        player.player1.bait += bait_purchase_amount
        print(
            f"You bought {bait_purchase_amount} bait. \nYou have ${player.player1.money} left.\n")

    def look_at_haul(self):
        player.player1.check_haul()


menu = MainMenu()
menu.menu_choice("y")
