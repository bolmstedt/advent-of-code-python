"""Solution for day 8, 2020."""
import re
from typing import List, Set, Tuple, Union

from app.base_solver import BaseSolver

INSTRUCTIONS = re.compile(r'^(\w{3}) ([+-]\d+)$', flags=re.MULTILINE)
NOOP = 0
JUMP = 1
ACC = 2
OPS = {
    'nop': NOOP,
    'jmp': JUMP,
    'acc': ACC,
}
SWITCH = {NOOP: JUMP, JUMP: NOOP}


class Solver(BaseSolver):
    """Solver for day 8, 2020."""

    day = '08'
    year = '2020'
    name = r"""Handheld Halting"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return self._solve(self._parse_input(data))[0]

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        instructions = self._parse_input(data)
        _, _, possible_indexes = self._solve(instructions, give_indexes=True)

        for index in possible_indexes:
            solution, finalized, _ = self._solve(instructions, switch_at=index)

            if finalized:
                return solution

        return 0

    @staticmethod
    def _solve(
        instructions: List[Tuple[int, int]],
        switch_at: int = None,
        give_indexes: bool = False,
    ) -> Tuple[int, bool, Set[int]]:
        acc = 0
        index = 0
        visited = set()
        possible_indexes: Set[int] = set()
        length = len(instructions)

        while index != length:
            if index in visited:
                return acc, False, possible_indexes

            instruction, modifier = instructions[index]
            visited.add(index)

            if (
                give_indexes and instruction != ACC and
                (
                    instruction == NOOP or
                    (instruction == JUMP and modifier < 1)
                )
            ):
                possible_indexes.add(index)

            if switch_at == index:
                instruction = SWITCH[instruction]

            if instruction == JUMP:
                index += modifier
                continue

            if instruction == ACC:
                acc += modifier

            index += 1

        return acc, True, set()

    @staticmethod
    def _parse_input(data: str) -> List[Tuple[int, int]]:
        return [
            (OPS[match[0]], int(match[1]))
            for match in INSTRUCTIONS.findall(data)
        ]
