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


menu = MainMenu()
menu.menu_choice("y")
