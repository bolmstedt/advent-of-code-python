"""Solution for day 1, 2020."""
from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 1, 2020."""

    def part_one(self, data: str) -> int:
        """Solve part one."""
        rows = self._parse_int_lines(data)

        while len(rows) > 0:
            first = rows.pop()

            for second in rows:
                if first + second == 2020:
                    return first * second

        return 0

    def part_two(self, data: str) -> int:
        """Solve part two."""
        rows = self._parse_int_lines(data)

        while len(rows) > 0:
            first = rows.pop()
            subset = rows.copy()

            while len(subset) > 0:
                second = subset.pop()

                for third in rows:
                    if first + second + third == 2020:
                        return first * second * third

        return 0
