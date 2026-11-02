from fish import Fish


def test_take_bait_reduces_by_one():
    fish1 = Fish()
    assert fish1.take_bait(5) == 4
    assert fish1.take_bait(1) == 0
