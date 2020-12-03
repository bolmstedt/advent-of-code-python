"""Solution for day 3, 2015."""
from typing import List, Union

from app.base_solver import BaseSolver


class _Sled:
    """Keeps track of a sled's position."""

    def __init__(self) -> None:
        self._x = 0
        self._y = 0

    @property
    def coords(self) -> str:
        """Get Santa's position."""
        return f'{self._x},{self._y}'

    def move(self, direction: str) -> str:
        """Move in one direction."""
        if direction == '^':
            self._y += 1
        elif direction == 'v':
            self._y -= 1
        elif direction == '<':
            self._x -= 1
        elif direction == '>':
            self._x += 1

        return self.coords


class Solver(BaseSolver):
    """Solver for day 3, 2015."""

    day = '03'
    year = '2015'
    name = r"""Perfectly Spherical Houses in a Vacuum"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._visit_houses(data, [_Sled()])

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._visit_houses(data, [_Sled(), _Sled()])

    @staticmethod
    def _visit_houses(data: str, sleds: List[_Sled]) -> int:
        grid = {sleds[0].coords}
        number_of_sleds = len(sleds)

        for index, sled in enumerate(sleds):
            for direction in data[index::number_of_sleds]:
                grid.add(sled.move(direction))

        return len(grid)
