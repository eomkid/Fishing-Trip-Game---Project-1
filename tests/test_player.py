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


def test_add_money_with_valid_fish():
    p = Player()
    p.add_money("Goldfish")
    assert p.money == 103


def test_add_money_with_invalid_fish(capsys):
    p = Player()
    p.add_money("Banana Fish")
    captured = capsys.readouterr()
    assert "Neither you, nor this program knows what fish you speak of" in captured.out
    assert p.money == 100
