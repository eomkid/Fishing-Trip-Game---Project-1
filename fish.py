from random import choice


class Fish:
    def __init__(self):
        self.fishes_and_prices = {"Black Crappie": 20, "Goldfish": 3, "Rainbow Trout": 50, "Rainbow Parrotfish": 25,
                                  "Bass": 10, "Lionfish": 50, "Squidward": 15, "Whale Shark": 100, "Orca": 99, "Nurse Shark": 70}

    def take_bait(self, bait: int):
        bait -= 1
        return bait

    def random_fish_pull(self, caught_or_not: bool, bait: int):
        if caught_or_not and bait >= 1:
            fish_caught = choice(list(self.fishes_and_prices))
            fish_price_check = self.fishes_and_prices[fish_caught]
            bait_left = self.take_bait(bait)
            return fish_caught, fish_price_check, bait_left

        elif caught_or_not and bait == 0:
            fish_caught = "Goldfish"
            fish_price_check = self.fishes_and_prices[fish_caught]
            return fish_caught, fish_price_check, bait

        elif not caught_or_not and bait >= 1:
            return None, 0, self.take_bait(bait)

        elif not caught_or_not and bait == 0:
            return None, 0, bait
