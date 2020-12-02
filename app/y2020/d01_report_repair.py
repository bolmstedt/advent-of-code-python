"""Solution for day 1, 2020."""
from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 1, 2020."""

    _limit = 2020

    def part_one(self, data: str) -> int:
        """Solve part one."""
        rows = self._parse_int_lines(data)

        while len(rows) > 0:
            first = rows.pop()

            if first > self._limit:
                continue

            for second in rows:
                if first + second == self._limit:
                    return first * second

        return 0

    def part_two(self, data: str) -> int:
        """Solve part two."""
        rows = self._parse_int_lines(data)

        while len(rows) > 0:
            first = rows.pop()

            if first > self._limit:
                continue

            for index, second in enumerate(rows):
                if first + second > self._limit:
                    continue

                for third in rows[index:]:
                    if first + second + third == self._limit:
                        return first * second * third

        return 0
