import player
import fish as fh


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
                play_state = "N"
                break
            if player_choice == 1:
                self.fish()
            if player_choice == 2:
                self.sell_fish()

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


menu = MainMenu()
menu.menu_choice("y")
