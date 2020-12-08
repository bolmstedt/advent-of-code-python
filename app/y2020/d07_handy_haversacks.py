"""Solution for day 7, 2020."""
import collections
import re
from typing import Dict, List, Set, Tuple, Union

from app.base_solver import BaseSolver

BAGS = re.compile(r'^(.*) bags contain (.*)$', flags=re.MULTILINE)
CONTENTS = re.compile(r'.*?(\d+) (.*?) bags?')
CHILDREN = re.compile(r'.*?\d+ (.*?) bags?')
TARGET_COLOR = 'shiny gold'


class Solver(BaseSolver):
    """Solver for day 7, 2020."""

    day = '07'
    year = '2020'
    name = r"""Handy Haversacks"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return len(self._get_bags_that_contain(
            self._parse_bags(data),
            TARGET_COLOR,
        ))

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._bags_in_bag(
            {
                bag.group(1): CONTENTS.findall(bag.group(2))
                for bag in BAGS.finditer(data)
            },
            TARGET_COLOR,
        )

    @classmethod
    def _get_bags_that_contain(
        cls,
        bags: Dict[str, List[str]],
        color: str,
    ) -> Set[str]:
        return set(bags[color]).union(*[
            cls._get_bags_that_contain(bags, _color) for _color in bags[color]
            if _color in bags
        ])

    @staticmethod
    def _parse_bags(data: str) -> Dict[str, List[str]]:
        bags: Dict[str, List[str]] = collections.defaultdict(list)

        for bag in BAGS.finditer(data):
            for child in CHILDREN.findall(bag.group(2)):
                bags[child].append(bag.group(1))

        return bags

    @classmethod
    def _bags_in_bag(
        cls,
        bags: Dict[str, List[Tuple[str, str]]],
        color: str,
    ) -> int:
        return sum(
            int(count) * (cls._bags_in_bag(bags, _color) + 1)
            for count, _color in bags[color]
        )
