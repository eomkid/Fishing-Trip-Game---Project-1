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


def test_save_and_load(tmp_path, monkeypatch):
    """Test that a save load restores the player data.
    """
    fake_save = tmp_path / "test_save.json"
    monkeypatch.setattr("player.save_file", fake_save)

    playey1 = Player()
    playey1.money = 250
    playey1.bait = 4
    playey1.fish_stored = ["Bass", "Goldfish"]
    playey1.name = "TestAngler"

    playey1.save()
    assert fake_save.exists()

    # Create a brand-new player and load into it
    player2 = Player()
    success = player2.load()
    assert success is True
    assert player2.money == 250
    assert player2.bait == 4
    assert player2.fish_stored == ["Bass", "Goldfish"]
    assert player2.name == "TestAngler"


def test_load_when_no_file_exists(tmp_path, monkeypatch, capsys):
    fake_save = tmp_path / "does_not_exist.json"
    monkeypatch.setattr("player.save_file", fake_save)

    player1 = Player()
    success = player1.load()
    assert success is False
    captured = capsys.readouterr()
    assert "No save file found" in captured.out
