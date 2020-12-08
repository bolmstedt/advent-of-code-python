"""Solution for day 8, 2020."""
import re
from typing import List, Tuple, Union

from app.base_solver import BaseSolver

INSTRUCTIONS = re.compile(r'^(\w{3}) ([+-]\d+)$', flags=re.MULTILINE)
NOOP = 'nop'
JUMP = 'jmp'
ACC = 'acc'
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

        for index, instruction in reversed(list(enumerate(instructions))):
            if instruction[0] == ACC:
                continue

            solution, finalized = self._solve(instructions, index)

            if finalized:
                return solution

        return 0

    @staticmethod
    def _solve(
        instructions: List[Tuple[str, int]],
        switch_at: int = None,
    ) -> Tuple[int, bool]:
        acc = 0
        index = 0
        visited = set()
        length = len(instructions)

        while index != length:
            if index in visited:
                return acc, False

            instruction, modifier = instructions[index]
            visited.add(index)

            if switch_at == index:
                instruction = SWITCH[instruction]

            if instruction == JUMP:
                index += modifier
                continue

            if instruction == ACC:
                acc += modifier

            index += 1

        return acc, True

    @staticmethod
    def _parse_input(data: str) -> List[Tuple[str, int]]:
        return [
            (match[0], int(match[1])) for match in INSTRUCTIONS.findall(data)
        ]
