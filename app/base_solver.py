"""Base class for day solvers."""
import abc
import re
from typing import List, Union

DIGITS = re.compile(r'\D')


class BaseSolver(abc.ABC):
    """Solves a day."""

    def __init__(self) -> None:
        parts = self.__module__.split('.')
        self._year = DIGITS.sub('', parts[1])
        self._day = DIGITS.sub('', parts[2][0:3])
        self._name = ' '.join([
            word.capitalize() for word in parts[2][4:].split('_')
        ])

    @property
    def year(self) -> str:
        """Get the year of this solver."""
        return self._year

    @property
    def day(self) -> str:
        """Get the day of this solver."""
        return self._day

    @property
    def name(self) -> str:
        """Get the name of this solver."""
        return self._name

    @property
    def full_name(self) -> str:
        """Get the full name of this solver."""
        return f'{self._year}:{self._day} - {self._name}'

    @abc.abstractmethod
    def part_one(self, data: str) -> Union[int, str]:
        """Return the solution for part one."""

    @abc.abstractmethod
    def part_two(self, data: str) -> Union[int, str]:
        """Return the solution for part two."""

    @staticmethod
    def _parse_int_lines(data: str) -> List[int]:
        return [int(val) for val in data.splitlines()]
