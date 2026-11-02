import json
from pathlib import Path
import pytest
from player import Player


def test_player_starts_with_correct_defaults():
    p = Player()
    assert p.money == 100
    assert p.bait == 0
    assert p.fish_stored == []
    assert p.name == "Player1"
