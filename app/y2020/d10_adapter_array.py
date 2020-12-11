"""Solution for day 10, 2020."""
import collections
from typing import Dict, List, Set, Union

from app.base_solver import BaseSolver


class Solver(BaseSolver):
    """Solver for day 10, 2020."""

    day = '10'
    year = '2020'
    name = r"""Adapter Array"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        jumps: Dict[int, int] = collections.defaultdict(int)
        adapters = self._parse_input(data)
        sequence = collections.deque(adapters[:1], 2)

        for adapter in adapters[1:]:
            sequence.append(adapter)

            jumps[sequence[1] - sequence[0]] += 1

        return jumps[1] * jumps[3]

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return self._solve_part_two(
            self._get_branches(self._parse_input(data)),
            {},
        )

    @staticmethod
    def _get_branches(adapters: List[int]) -> Dict[int, Set[int]]:
        branches = collections.defaultdict(set)

        for index, adapter in enumerate(adapters):
            max_jump = adapter + 3

            for upcoming in adapters[index + 2:index + 4]:
                if upcoming <= max_jump:
                    branches[adapter].add(upcoming)

        return branches

    @classmethod
    def _solve_part_two(
        cls,
        branches: Dict[int, Set[int]],
        solved: Dict[Union[int, str], int],
        start: int = 0,
    ) -> int:
        if start not in solved:
            arrangements = 1

            for adapter, jumps in branches.items():
                if adapter < start:
                    continue

                for jump in jumps:
                    branch = f'{adapter}:{jump}'

                    if branch not in solved:
                        solved[branch] = cls._solve_part_two(
                            branches,
                            solved,
                            jump,
                        )

                    arrangements += solved[branch]
            solved[start] = arrangements

        return solved[start]

    @classmethod
    def _parse_input(cls, data: str) -> List[int]:
        adapters = cls._parse_int_lines(data)

        return sorted(adapters + [0, max(adapters) + 3])
