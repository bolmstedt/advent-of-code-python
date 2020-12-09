"""Solution for day 9, 2020."""
import collections
import itertools
from typing import List, Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 9, 2020."""

    day = '09'
    year = '2020'
    name = r"""Encoding Error"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve_part_one(self._parse_input(data), 25)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        values = self._parse_input(data)
        return self._solve_part_two(values, self._solve_part_one(values, 25))

    @staticmethod
    def _solve_part_one(values: List[int], preamble_length: int) -> int:
        preamble = collections.deque(values[:preamble_length], preamble_length)

        for value in values[preamble_length:]:
            missing = True

            for combination in itertools.combinations(preamble, 2):
                if sum(combination) == value:
                    missing = False
                    break

            if missing:
                return value

            preamble.append(value)

        return 0

    @staticmethod
    def _solve_part_two(values: List[int], target: int) -> int:
        length = len(values)

        for start in range(length):
            for stop in range(len(values[start:])):
                contiguous = values[start:stop]
                total = sum(contiguous)

                if total > target:
                    break
                elif total == target:
                    return min(contiguous) + max(contiguous)

        return 0

    @staticmethod
    def _parse_input(data: str) -> List[int]:
        return [int(value) for value in data.splitlines()]
