"""Custom tests for day 21, 2015."""
from app.y2015.d21_rpg_simulator_20xx import Fighter, Item, Solver


def test_battle_player_win() -> None:
    """Assert that the player wins."""
    player = Fighter(hp=8, damage=5, armor=5)
    boss = Fighter(hp=12, damage=7, armor=2)
    assert Solver()._battle(player, boss, [])


def test_battle_boss_win() -> None:
    """Assert that the boss wins."""
    player = Fighter(hp=8, damage=5, armor=5)
    boss = Fighter(hp=12, damage=7, armor=3)
    assert not Solver()._battle(player, boss, [])


def test_battle_loadout_win() -> None:
    """Assert that the player wins with an item."""
    player = Fighter(hp=8, damage=5, armor=5)
    boss = Fighter(hp=12, damage=7, armor=3)
    assert Solver()._battle(
        player,
        boss,
        [Item(cost=0, damage=1, armor=0)],
    )


def test_battle_complex_loadout_win() -> None:
    """Assert that the player wins with a complex loadout."""
    player = Fighter(hp=100, damage=0, armor=0)
    boss = Fighter(hp=103, damage=9, armor=2)
    assert Solver()._battle(
        player,
        boss,
        [
            Item(cost=0, damage=7, armor=0),
            Item(cost=0, damage=0, armor=2),
            Item(cost=0, damage=2, armor=0),
            Item(cost=0, damage=0, armor=0),
        ],
    )


def test_battle_maximum_armor() -> None:
    """Assert that the boss wins."""
    player = Fighter(hp=8, damage=1, armor=100)
    boss = Fighter(hp=12, damage=1, armor=3)
    assert not Solver()._battle(player, boss, [])
