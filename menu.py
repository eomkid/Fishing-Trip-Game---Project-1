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


menu = MainMenu()
menu.menu_display()
