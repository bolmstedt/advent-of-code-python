"""Solution for day 5, 2020."""
from typing import List, Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 5, 2020."""

    day = '05'
    year = '2020'
    name = r"""Binary Boarding"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._parse_seats(data)[-1]

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        seats = self._parse_seats(data)

        return set(range(seats[0], seats[-1])).difference(seats).pop()

    @classmethod
    def _parse_seats(cls, data: str) -> List[int]:
        return sorted(
            int(seat, 2) for seat in cls._to_binary(data).splitlines()
        )

    @staticmethod
    def _to_binary(data: str) -> str:
        return data.replace(
            'F', '0',
        ).replace(
            'B', '1',
        ).replace(
            'L', '0',
        ).replace(
            'R', '1',
        )
