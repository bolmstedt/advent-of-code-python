"""Solution for day 6, 2015."""
import re
from typing import Callable, List, Tuple, Union

from app.base_solver import BaseSolver

LIGHTS_PER_ROW = 1000
ROWS = 1000
OPERATION = re.compile(r'(.*) (\d+,\d+).*?(\d+,\d+)')

SliceType = List[Tuple[int, int]]


class Solver(BaseSolver):
    """Solver for day 6, 2015."""

    day = '06'
    year = '2015'
    name = r"""Probably a Fire Hazard"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve(
            data,
            [False] * (ROWS * LIGHTS_PER_ROW),
            self._solve_one,
        )

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._solve(
            data,
            [0] * (ROWS * LIGHTS_PER_ROW),
            self._solve_two,
        )

    @classmethod
    def _solve(
        cls,
        data: str,
        grid: Union[List[bool], List[int]],
        method: Callable,
    ) -> int:
        instructions = data.splitlines()

        for instruction in instructions:
            operation, slices = cls._parse_instruction(instruction)
            method(grid, operation, slices)

        return sum(grid)

    @staticmethod
    def _solve_one(
        grid: List[bool],
        operation: str,
        slices: SliceType,
    ) -> None:
        if operation == 'toggle':
            for span in slices:
                for pos in range(span[0], span[1]):
                    grid[pos] = not grid[pos]
        else:
            value = [operation == 'turn on']

            for span in slices:
                grid[span[0]:span[1]] = value * (span[1] - span[0])

    @staticmethod
    def _solve_two(
        grid: List[int],
        operation: str,
        slices: SliceType,
    ) -> None:
        if operation == 'turn off':
            for span in slices:
                for pos in range(span[0], span[1]):
                    grid[pos] = max(0, grid[pos] - 1)
        else:
            if operation == 'turn on':
                value = 1
            else:
                value = 2

            for span in slices:
                for pos in range(span[0], span[1]):
                    grid[pos] += value

    @staticmethod
    def _parse_instruction(
        instruction: str,
    ) -> Tuple[str, SliceType]:
        match = OPERATION.match(instruction)

        if not match:
            raise ValueError('Unknown instruction')

        operation = match.group(1)
        upper = list(map(int, match.group(2).split(',')))
        lower = list(map(int, match.group(3).split(',')))
        rows = range(upper[1] * ROWS, lower[1] * ROWS + 1, ROWS)
        slices = [(upper[0] + row, lower[0] + row + 1) for row in rows]

        return operation, slices
