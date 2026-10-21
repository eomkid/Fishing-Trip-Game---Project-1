from random import randint


class Fish:
    def __init__(self):
        self.fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                                  "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

    def catch_check(self):
        catch_or_not = randint(0, 1)
        if catch_or_not == 1:
            return True
        else:
            return False

    def take_bait(self):
        pass
