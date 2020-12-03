"""Solution for day 2, 2020."""
import re
from typing import Union

from app.base_solver import BaseSolver

PASSWORD = re.compile(r'\W+')


class Solver(BaseSolver):
    """Solver for day 2, 2020."""

    day = '02'
    year = '2020'
    name = r"""Password Philosophy"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        rows = data.splitlines()

        valid_passwords = 0

        for row in rows:
            lower_limit, upper_limit, letter, password = PASSWORD.split(row)

            if int(lower_limit) <= password.count(letter) <= int(upper_limit):
                valid_passwords += 1

        return valid_passwords

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        rows = data.splitlines()

        valid_passwords = 0

        for row in rows:
            first, second, letter, password = PASSWORD.split(row)
            first_position = int(first) - 1
            second_position = int(second) - 1

            if (
                password[first_position] == letter and
                password[second_position] != letter
            ) or (
                password[first_position] != letter and
                password[second_position] == letter
            ):
                valid_passwords += 1

        return valid_passwords
