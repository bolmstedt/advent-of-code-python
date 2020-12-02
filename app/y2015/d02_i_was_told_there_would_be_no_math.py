"""Solution for day 02, 2015."""
import itertools
import math
from typing import Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 02, 2015."""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        rows = data.strip().splitlines()
        paper = 0

        for row in rows:
            factors = list(map(int, row.split('x')))
            combinations = itertools.combinations(factors, 2)
            faces = [math.prod(sides) for sides in combinations]
            paper += sum(faces) * 2 + min(faces)

        return paper

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        rows = data.strip().splitlines()
        ribbon = 0

        for row in rows:
            sides = sorted(map(int, row.split('x')))
            ribbon += sum(sides[:2]) * 2 + math.prod(sides)

        return ribbon
