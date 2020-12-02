"""Solution for day 1, 2019."""
import math
from typing import Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 1, 2019."""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        modules = self._parse_int_lines(data)

        return sum(map(self._get_fuel_consumption, modules))

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        modules = self._parse_int_lines(data)

        return sum(map(self._get_compensated_fuel_consumption, modules))

    @staticmethod
    def _get_fuel_consumption(mass: int) -> int:
        return max(0, math.floor(mass / 3) - 2)

    @classmethod
    def _get_compensated_fuel_consumption(cls, mass: int) -> int:
        total_fuel = fuel = cls._get_fuel_consumption(mass)

        while True:
            fuel = cls._get_fuel_consumption(fuel)

            if fuel == 0:
                return total_fuel

            total_fuel += fuel
