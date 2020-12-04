"""Solution for day 4, 2015."""
import itertools
from typing import Union

from _md5 import md5

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 4, 2015."""

    day = '04'
    year = '2015'
    name = r"""The Ideal Stocking Stuffer"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        target = bytearray([0, 0, 16])

        for index in itertools.count():
            if md5(f'{data}{index}'.encode('ascii')).digest()[0:3] < target:
                return index

        return 0

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        target = bytearray([0, 0, 0])

        for index in itertools.count():
            if md5(f'{data}{index}'.encode()).digest().startswith(target):
                return index

        return 0
