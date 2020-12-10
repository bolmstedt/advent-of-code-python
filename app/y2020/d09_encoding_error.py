"""Solution for day 9, 2020."""
import collections
from typing import Deque, List, Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 9, 2020."""

    day = '09'
    year = '2020'
    name = r"""Encoding Error"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve_part_one(self._parse_int_lines(data), 25)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        values = self._parse_int_lines(data)

        return self._solve_part_two(values, self._solve_part_one(values, 25))

    @staticmethod
    def _solve_part_one(values: List[int], preamble_length: int) -> int:
        preamble = collections.deque(values[:preamble_length], preamble_length)

        for value in values[preamble_length:]:
            min_value = value - min(preamble)

            for sub_value in preamble:
                if sub_value <= min_value:
                    preamble.append(value)
                    break
            else:
                return value

        return 0

    @staticmethod
    def _solve_part_two(values: List[int], target: int) -> int:
        contiguous: Deque[int] = collections.deque()
        total = 0
        half_target = target / 2

        for value in values:
            if value >= half_target:
                continue

            contiguous.append(value)
            total += value

            while total > target:
                total -= contiguous.popleft()

            if total == target:
                return min(contiguous) + max(contiguous)

        return 0
