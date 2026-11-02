from random import randint
from fish import Fish


class Player:
    def __init__(self):
        self.money = 100
        self.fish_stored = []
        self.bait = 0
        self.name = "Player1"

    def catch_check(self):
        catch_or_not = randint(0, 1)
        if catch_or_not == 1:
            return True
        else:
            return False

    def fishing_action(self):
        fish = Fish()
        catch_or_not = self.catch_check()
        fish_caught, fish_price_check, bait_left = fish.random_fish_pull(
            catch_or_not, bait=self.bait)
        if fish_caught != "":
            self.fish_stored.append(fish_caught)
        self.bait = bait_left
        return fish_caught, fish_price_check

    def add_money(self, fish_to_sell: str):
        fish = Fish()
        if fish_to_sell != "" and fish_to_sell in fish.fishes_and_prices:
            self.money += fish.fishes_and_prices[fish_to_sell]
        else:
            print(f"Neither you, nor this program knows what fish you speak of")

    def take_money(self, money_taken: int):
        if self.money >= money_taken:
            self.money -= money_taken
        else:
            print(
                f"You don't have enough money for that. \nYou only have ${self.money}")

    def check_money(self):
        print(f"\nYou have ${self.money}")
        print("...")
        print("So are you willing to share?\n")

    def check_haul(self):
        if self.fish_stored != []:
            print("You have mighty haul here \nSo far you've caught:")
            for fish in self.fish_stored:
                print(fish)
        elif self.fish_stored == []:
            print("I've been looking for like 5 whole nanoseconds and I dont see anything in here\n"
                  "Maybe try catching something before you try looking at your haul.")


player1 = Player()
