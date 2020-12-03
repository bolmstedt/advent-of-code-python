"""Base class for day solvers."""
import abc
import re
from typing import List, Union

DIGITS = re.compile(r'\D')


class BaseSolver(abc.ABC):
    """Solves a day."""

    day: str
    year: str
    name: str

    @property
    def full_name(self) -> str:
        """Get the full name of this solver."""
        return f'{self.year}:{self.day} - {self.name}'

    @abc.abstractmethod
    def part_one(self, data: str) -> Union[int, str]:
        """Return the solution for part one."""

    @abc.abstractmethod
    def part_two(self, data: str) -> Union[int, str]:
        """Return the solution for part two."""

    @staticmethod
    def _parse_int_lines(data: str) -> List[int]:
        return [int(val) for val in data.splitlines()]
