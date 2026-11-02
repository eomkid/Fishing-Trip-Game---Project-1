import json
from pathlib import Path
import pytest
from player import Player


def test_player_starts_with_correct_defaults():
    player1 = Player()
    assert player1.money == 100
    assert player1.bait == 0
    assert player1.fish_stored == []
    assert player1.name == "Player1"


def test_add_money_with_valid_fish():
    player1 = Player()
    player1.add_money("Goldfish")
    assert player1.money == 103


def test_add_money_with_invalid_fish(capsys):
    player1 = Player()
    player1.add_money("Banana Fish")
    captured = capsys.readouterr()
    assert "Neither you, nor this program knows what fish you speak of" in captured.out
    assert player1.money == 100


def test_take_money_enough_money():
    player1 = Player()
    player1.take_money(40)
    assert player1.money == 60


def test_take_money_not_enough(capsys):
    player1 = Player()
    player1.take_money(150)
    captured = capsys.readouterr()
    assert "You don't have enough money" in captured.out
    assert player1.money == 100
