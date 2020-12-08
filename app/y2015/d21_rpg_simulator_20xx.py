"""Solution for day 21, 2015."""
import itertools
import math
import re
from typing import List, TypedDict, Union

from app.base_solver import BaseSolver

ITEM = re.compile(r'^.+?\s+(\d+).+?(\d+).+?(\d+)$', flags=re.MULTILINE)
BOSS = re.compile(r'.+?(\d+).+?(\d+).+?(\d+)', flags=re.DOTALL)


class Fighter(TypedDict):
    """Typed dictionary for fighters."""

    hp: int
    damage: int
    armor: int


class Item(TypedDict):
    """Typed dictionary for items."""

    cost: int
    damage: int
    armor: int


class Solver(BaseSolver):
    """Solver for day 21, 2015."""

    day = '21'
    year = '2015'
    name = r"""RPG Simulator 20XX"""

    def __init__(self) -> None:
        with open('input/2015/21/shop.txt', 'r') as handle:
            shop = handle.read().split('\n\n')

        weapons = [
            Item(cost=int(item[0]), damage=int(item[1]), armor=int(item[2]))
            for item in ITEM.findall(shop[0])
        ]

        armors = [
            Item(cost=int(item[0]), damage=int(item[1]), armor=int(item[2]))
            for item in ITEM.findall(shop[1])
        ] + [Item(cost=0, damage=0, armor=0)]

        rings = [
            Item(cost=int(item[0]), damage=int(item[1]), armor=int(item[2]))
            for item in ITEM.findall(shop[2])
        ] + [Item(cost=0, damage=0, armor=0), Item(cost=0, damage=0, armor=0)]

        self._shop = [
            [weapon, armor, ring[0], ring[1]]
            for weapon in weapons
            for armor in armors
            for ring in itertools.combinations(rings, 2)
        ]

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        boss = self._parse_boss(data)
        player = Fighter(hp=100, damage=0, armor=0)

        return min(
            sum(item['cost'] for item in loadout)
            for loadout in self._shop
            if self._battle(player, boss, loadout)
        )

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        boss = self._parse_boss(data)
        player = Fighter(hp=100, damage=0, armor=0)

        return max(
            sum(item['cost'] for item in loadout)
            for loadout in self._shop
            if not self._battle(player, boss, loadout)
        )

    @staticmethod
    def _parse_boss(data: str) -> Fighter:
        boss_match = BOSS.search(data)

        if not boss_match:
            raise ValueError('Found no boss data.')

        return Fighter(
            hp=int(boss_match.group(1)),
            damage=int(boss_match.group(2)),
            armor=int(boss_match.group(3)),
        )

    @staticmethod
    def _battle(
        player: Fighter,
        boss: Fighter,
        loadout: List[Item],
    ) -> bool:
        _player = player.copy()
        _boss = boss.copy()

        for item in loadout:
            _player['damage'] += item['damage']
            _player['armor'] += item['armor']

        _player['damage'] = max(1, _player['damage'] - _boss['armor'])
        _boss['damage'] = max(1, _boss['damage'] - _player['armor'])

        return (
            math.ceil(_boss['hp'] / _player['damage']) <=
            math.ceil(player['hp'] / _boss['damage'])
        )
