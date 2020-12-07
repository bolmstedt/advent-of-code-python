"""Solution for day 6, 2020."""
from typing import Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 6, 2020."""

    day = '06'
    year = '2020'
    name = r"""Custom Customs"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        newline = set('\n')

        return sum(len(set(group) - newline) for group in data.split('\n\n'))

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return sum(
            len(set.intersection(
                *[set(person) for person in group.splitlines()],
            )) for group in data.split('\n\n')
        )
