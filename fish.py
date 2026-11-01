class Fish:
    def __init__(self):
        self.fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                                  "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

    def take_bait(self, bait):
        bait -= 1
        return bait
