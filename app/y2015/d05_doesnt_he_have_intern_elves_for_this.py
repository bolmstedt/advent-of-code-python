"""Solution for day 5, 2015."""
import re
from typing import Union

from app.base_solver import BaseSolver

NICE_STRING = re.compile(
    r'(?=.*([\w])\1)(?=(?:.*[aeiou]){3,})(?!.*(?:ab|cd|pq|xy))^.+$',
)
REALLY_NICE_STRING = re.compile(r'(?=.*(\w{2}).*\1)(?=.*(\w)\w\2)^.+$')


class Solver(BaseSolver):
    """Solver for day 5, 2015."""

    day = '05'
    year = '2015'
    name = r"""Doesn't He Have Intern-Elves For This?"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return sum(
            self._is_nice(NICE_STRING, string)
            for string in data.splitlines()
        )

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return sum(
            self._is_nice(REALLY_NICE_STRING, string)
            for string in data.splitlines()
        )

    @staticmethod
    def _is_nice(pattern: re.Pattern, string: str) -> bool:
        return pattern.search(string) is not None
