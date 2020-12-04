"""Solution for day 6, 2015."""
import re
from typing import Any, Generator, Tuple, Union

from app.base_solver import BaseSolver

LIGHTS_PER_ROW = 1000
ROWS = 1000
OPERATION = re.compile(r'(.*) (\d+,\d+).*?(\d+,\d+)')


class Solver(BaseSolver):
    """Solver for day 6, 2015."""

    day = '06'
    year = '2015'
    name = r"""Probably a Fire Hazard"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        instructions = data.splitlines()
        grid = [False] * (ROWS * LIGHTS_PER_ROW)

        for instruction in instructions:
            operation, slices = self._parse_instruction(instruction)

            for span in slices:
                if operation == 'toggle':
                    for pos in range(span[0], span[1]):
                        grid[pos] = not grid[pos]
                else:
                    grid[span[0]:span[1]] = [
                        operation == 'turn on',
                    ] * (span[1] - span[0])

        return sum(grid)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        instructions = data.splitlines()
        grid = [0] * (ROWS * LIGHTS_PER_ROW)

        for instruction in instructions:
            operation, slices = self._parse_instruction(instruction)

            for span in slices:
                for pos in range(span[0], span[1]):
                    if operation == 'turn on':
                        grid[pos] += 1
                    elif operation == 'turn off':
                        grid[pos] = max(0, grid[pos] - 1)
                    else:
                        grid[pos] += 2

        return sum(grid)

    @staticmethod
    def _parse_instruction(
        instruction: str,
    ) -> Tuple[str, Generator[Tuple[int, int], Any, None]]:
        match = OPERATION.match(instruction)

        if not match:
            raise ValueError('Unknown instruction')

        operation = match.group(1)
        upper = list(map(int, match.group(2).split(',')))
        lower = list(map(int, match.group(3).split(',')))
        rows = range(upper[1] * ROWS, lower[1] * ROWS + 1, ROWS)
        slices = ((upper[0] + row, lower[0] + row + 1) for row in rows)

        return operation, slices
