from random import randint


class Player:
    def __init__(self):
        self.money = 100
        self.fish_stored = []
        self.bait = 0
        self.name = "Player1"

    def fish(self, bait):

        pass

    def catch_check(self):
        catch_or_not = randint(0, 1)
        if catch_or_not == 1:
            return True
        else:
            return False
