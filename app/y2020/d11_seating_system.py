"""Solution for day 11, 2020."""
import itertools
from typing import List, Union

from app.base_solver import BaseSolver

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = set(itertools.permutations([-1, -1, 0, 1, 1], 2))


class Solver(BaseSolver):
    """Solver for day 11, 2020."""

    day = '11'
    year = '2020'
    name = r"""Seating System"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve([list(line) for line in data.splitlines()])

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._solve([list(line) for line in data.splitlines()], True)

    @classmethod
    def _solve(cls, rows: List[List[str]], sight: bool = False) -> int:
        new_state: List[List[str]] = []
        height = len(rows)
        width = len(rows[0])

        for row_index, row in enumerate(rows):
            new_row = []

            for col_index, seat in enumerate(row):
                if seat == FLOOR:
                    new_row.append(seat)
                    continue

                if sight:
                    surroundings = []

                    for x_dir, y_dir in DIRECTIONS:
                        for x_pos, y_pos in zip(
                            itertools.count(col_index + x_dir, x_dir),
                            itertools.count(row_index + y_dir, y_dir),
                        ):
                            if (
                                x_pos < 0 or x_pos >= width or
                                y_pos < 0 or y_pos >= height
                            ):
                                break

                            if rows[y_pos][x_pos] != FLOOR:
                                surroundings.append(rows[y_pos][x_pos])
                                break
                else:
                    surroundings = [
                        _seat
                        for _row in rows[max(0, row_index - 1):row_index + 2]
                        for _seat in _row[max(0, col_index - 1):col_index + 2]
                    ]
                    surroundings.remove(seat)

                occupied = surroundings.count(OCCUPIED)

                if occupied == 0:
                    seat = OCCUPIED
                elif (
                    not sight and occupied >= 4 or
                    sight and occupied >= 5
                ):
                    seat = EMPTY

                new_row.append(seat)

            new_state.append(new_row)

        if new_state != rows:
            return cls._solve(new_state, sight)

        return sum(row.count(OCCUPIED) for row in rows)
