"""Solution for day 3, 2020."""
import math
from typing import List, Union

from app.base_solver import BaseSolver

TREE = '#'


class Solver(BaseSolver):
    """Solver for day 3, 2020."""

    day = '03'
    year = '2020'
    name = r"""Toboggan Trajectory"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._get_hit_trees(data.splitlines(), 3, 1)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return math.prod([
            self._get_hit_trees(data.splitlines(), speed_x, speed_y)
            for speed_x, speed_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ])

    @staticmethod
    def _get_hit_trees(rows: List[str], speed_x: int, speed_y: int) -> int:
        map_width = len(rows[0])

        return sum(
            row[speed_x * y % map_width] == TREE
            for y, row in enumerate(rows[0::speed_y][1:], start=1)
        )
