"""Solution for day 2, 2020."""
from typing import Callable, Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 2, 2020."""

    day = '02'
    year = '2020'
    name = r"""Password Philosophy"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve(data, self._letter_appears_times)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._solve(data, self._letter_appears_only_once_at)

    @staticmethod
    def _solve(
        data: str,
        validation: Callable[[int, int, str, str], bool],
    ) -> int:
        valid_passwords = 0

        for row in data.splitlines():
            parts = row.split(' ', 1)
            rules = parts[0].split('-')

            if validation(
                int(rules[0]),
                int(rules[1]),
                parts[1][:1],
                parts[1][3:],
            ):
                valid_passwords += 1

        return valid_passwords

    @staticmethod
    def _letter_appears_times(
        lower: int,
        upper: int,
        letter: str,
        password: str,
    ) -> bool:
        return lower <= password.count(letter) <= upper

    @staticmethod
    def _letter_appears_only_once_at(
        first: int,
        second: int,
        letter: str,
        password: str,
    ) -> bool:
        return (
            password[first - 1] == letter or
            password[second - 1] == letter
        ) and password[first - 1] != password[second - 1]
