"""Solution for day 3, 2015."""
from typing import Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 3, 2015."""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        santa = _Position()
        grid = {santa.coords}

        for direction in data:
            grid.add(santa.move(direction))

        return len(grid)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        santa = _Position()
        robo_santa = _Position()
        grid = {santa.coords}

        for index, direction in enumerate(data):
            if index % 2 == 0:
                grid.add(santa.move(direction))
            else:
                grid.add(robo_santa.move(direction))

        return len(grid)


class _Position:
    """Keeps track of Santa's position."""

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    @property
    def coords(self) -> str:
        """Get Santa's position."""
        return f'{self.x},{self.y}'

    def move(self, direction: str) -> str:
        """Move in one direction."""
        if direction == '^':
            self.y += 1
        if direction == 'v':
            self.y -= 1
        if direction == '<':
            self.x -= 1
        if direction == '>':
            self.x += 1

        return self.coords
