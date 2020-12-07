"""Solution for day 7, 2020."""
import re
from typing import Dict, List, Set, Tuple, Union

from app.base_solver import BaseSolver

BAGS = re.compile(r'(.*) bags contain (.*)')
CONTENTS = re.compile(r'.*?(\d+) (.*?) bags?')


class Solver(BaseSolver):
    """Solver for day 7, 2020."""

    day = '07'
    year = '2020'
    name = r"""Handy Haversacks"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        rules = {
            color: {c[1] for c in contents}
            for color, contents in self._parse_rules(data).items()
        }
        return len(self._get_bags_that_can_contain(
            rules,
            'shiny gold',
        ))

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._bags_in_bag(self._parse_rules(data), 'shiny gold')

    @classmethod
    def _get_bags_that_can_contain(
        cls,
        rules: Dict[str, Set[str]],
        color: str,
    ) -> Set[str]:
        new_bags = {
            bag for bag, contents in rules.items()
            if color in contents
        }

        for bag in new_bags:
            del rules[bag]

        return new_bags.union(*[
            cls._get_bags_that_can_contain(rules, c) for c in new_bags
        ])

    @classmethod
    def _bags_in_bag(
        cls,
        bags: Dict[str, List[Tuple[str, str]]],
        color: str,
    ) -> int:
        return sum(
            int(count) + int(count) * cls._bags_in_bag(bags, c)
            for count, c in bags[color]
        )

    @staticmethod
    def _parse_rules(data: str) -> Dict[str, List[Tuple[str, str]]]:
        rules = {}

        for rule in data.splitlines():
            bag_matches = BAGS.search(rule)

            if not bag_matches:
                continue

            groups = bag_matches.groups()

            rules[groups[0]] = CONTENTS.findall(groups[1])

        return rules
