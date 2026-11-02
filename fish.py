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
            print(
                f"Nice nice, you caught a {fish_caught} I would say you could sell it for about ${fish_price_check}")
            return fish_caught, fish_price_check, bait_left

        elif caught_or_not and bait == 0:
            fish_caught = "Goldfish"
            fish_price_check = self.fishes_and_prices[fish_caught]
            print(
                f"You caught a {fish_caught} :| \nIt's not worth much only ${fish_price_check}\n")
            return fish_caught, fish_price_check, bait

        elif not caught_or_not and bait >= 1:
            print("Dang that fish was such a monster it snapped the line and stole the bait.\n What a waste of good bait.")
            return "", 0, self.take_bait(bait)

        elif not caught_or_not and bait == 0:
            print("Don't ask me how... \nBut the Goldfish broke the line and got away \nYou might wanna get a better fishing line just saying.")
            return "", 0, bait
        else:
            return "", 0, bait
