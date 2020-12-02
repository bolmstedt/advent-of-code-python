"""Solution for day 1, 2015."""
from typing import Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 1, 2019."""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return data.count('(') - data.count(')')

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        floor = 0

        for index, direction in enumerate(data):
            if direction == '(':
                floor += 1
            else:
                floor -= 1

            if floor < 0:
                return index + 1

        return 0
