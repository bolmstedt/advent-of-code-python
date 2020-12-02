#!/usr/bin/env python3
"""Advent of Code solutions."""
import sys
import time
from enum import Enum
from pathlib import Path

from app import utils

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


class Action(Enum):
    """Enumerations for actions."""

    SOLVE = 'solve'


def _main(action: Action) -> None:
    if action == Action.SOLVE:
        _solve()


def _solve(only: str = None) -> None:
    solvers = utils.load_solvers()

    for year, days in solvers.items():
        for day, solver in days.items():
            if only and f'{year}:{day}' != only:
                continue

            _cprint(solver.full_name, HEADER)

            data_file = Path(f'input/{year}/{day}/input.txt')

            if not data_file.is_file():
                _cprint('\tSkipped', WARNING)
                continue

            with open(data_file, 'r') as handle:
                data = handle.read().strip()

            start = time.perf_counter()
            part_one = solver.part_one(data)
            part_one_time = round((time.perf_counter() - start) * 1000, 2)

            start = time.perf_counter()
            part_two = solver.part_two(data)
            part_two_time = round((time.perf_counter() - start) * 1000, 2)

            if not part_one:
                part_one = '-'

            if not part_two:
                part_two = '-'

            _cprint(f'\tPart One: {part_one} ({part_one_time}ms)', OKGREEN)
            _cprint(f'\tPart Two: {part_two} ({part_two_time}ms)', OKGREEN)


def _cprint(text: str, color: str = None) -> None:
    if not color:
        color = ''

    print(f'{color}{text}{ENDC}')  # noqa: T001


def _help() -> None:
    _cprint('Advent of Code Solutions')
    _cprint('Usage', BOLD)
    _cprint('\tpython main.py')


if __name__ == '__main__':
    _action = Action.SOLVE
    _args = sys.argv[1:]

    if len(_args) == 0:
        _main(_action)
        sys.exit(0)

    _current_arg = _args.pop(0)

    try:
        _action = Action[_current_arg]
    except KeyError:
        _cprint(f'"{_current_arg}" is not a valid action.', FAIL)
        sys.exit(1)

    _main(_action)
