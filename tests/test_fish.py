from fish import Fish


def test_take_bait_reduces_by_one():
    fish1 = Fish()
    assert fish1.take_bait(5) == 4
    assert fish1.take_bait(1) == 0


def test_random_fish_pull_with_bait_and_catch():
    fish1 = Fish()
    fish, price, bait_left = fish1.random_fish_pull(True, bait=3)
    assert fish in fish1.fishes_and_prices
    assert price == fish1.fishes_and_prices[fish]
    assert bait_left == 2


def test_random_fish_pull_no_bait_but_catch():
    fish1 = Fish()
    fish, price, bait_left = fish1.random_fish_pull(True, bait=0)
    assert fish == "Goldfish"
    assert price == 3
    assert bait_left == 0
