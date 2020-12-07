"""Solution for day 7, 2020."""
import re
from typing import Dict, List, Tuple, Union

from app.base_solver import BaseSolver

BAGS = re.compile(r'^(.*) bags contain (.*)$', flags=re.MULTILINE)
CONTENTS = re.compile(r'.*?(\d+) (.*?) bags?')
TARGET_COLOR = 'shiny gold'


class _RuleSet:
    """Helper class for a set of rules."""

    def __init__(self, data: str):
        self._bags = self._parse_bags(data)
        self._plain_bags = {
            color: {c[1] for c in contents}
            for color, contents in self._bags.items()
        }

    def get_bags_that_can_contain(
        self,
        color: str,
    ) -> int:
        new_bags = {
            bag for bag, contents in self._plain_bags.items()
            if color in contents
        }

        for bag in new_bags:
            del self._plain_bags[bag]

        return len(new_bags) + sum(
            self.get_bags_that_can_contain(c) for c in new_bags
        )

    def bags_in_bag(
        self,
        color: str,
    ) -> int:
        return sum(
            int(count) * (self.bags_in_bag(_color) + 1)
            for count, _color in self._bags[color]
        )

    @staticmethod
    def _parse_bags(data: str) -> Dict[str, List[Tuple[str, str]]]:
        return {
            bags.group(1): CONTENTS.findall(bags.group(2))
            for bags in BAGS.finditer(data)
        }


class Solver(BaseSolver):
    """Solver for day 7, 2020."""

    day = '07'
    year = '2020'
    name = r"""Handy Haversacks"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return _RuleSet(data).get_bags_that_can_contain(TARGET_COLOR)

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return _RuleSet(data).bags_in_bag(TARGET_COLOR)
