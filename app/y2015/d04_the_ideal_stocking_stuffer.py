"""Solution for day 4, 2015."""
from typing import Union

from _md5 import md5

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 4, 2015."""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve(data, 5)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._solve(data, 6)

    @staticmethod
    def _solve(data: str, zeroes: int) -> int:
        target = ''.zfill(zeroes)
        index = 0

        while True:
            if md5(f'{data}{index}'.encode()).hexdigest().startswith(target):
                return index

            index += 1
