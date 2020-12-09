"""Console commands."""
import html
import os
import re
import sys
import time
from pathlib import Path

import requests

from app import utils

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

AOC_WEB = 'https://adventofcode.com/{year}/day/{day}'


def solutions() -> None:
    """Display all solutions."""
    solvers = utils.load_solvers()

    for days in solvers.values():
        for solver in days.values():
            _cprint(solver.full_name, HEADER)


def solve() -> None:
    """Solve solutions."""
    args = sys.argv[1:]

    if len(args) < 1:
        _cprint('Specify "all" to run all dates, or', FAIL)
        _cprint('Specify a solution year in the format "YYYY", or', FAIL)
        _cprint('Specify a solution date in the format "YYYY:DD"', FAIL)
        sys.exit(1)

    solution = args[0]

    if len(args) > 2 and args[1] == '--loops':
        loops = int(args[2])
    else:
        loops = 1

    solvers = utils.load_solvers()

    for year, days in solvers.items():
        for day, solver in days.items():
            if (
                solution and solution != 'all' and
                f'{year}:{day}' != solution and year != solution
            ):
                continue

            _cprint(solver.full_name, HEADER)

            try:
                data = utils.load_input(solver, 'input')
            except FileNotFoundError:
                _cprint('\tSkipped', WARNING)
                continue

            start = time.perf_counter()

            for _ in range(loops):
                part_one = solver.part_one(data)

            part_one_time = round(
                (time.perf_counter() - start) / loops * 1000,
                2,
            )

            if not part_one:
                part_one = 'Not done'

            _cprint(f'\tPart One: {part_one} ({part_one_time}ms)', OKGREEN)

            start = time.perf_counter()

            for _ in range(loops):
                part_two = solver.part_two(data)

            part_two_time = round(
                (time.perf_counter() - start) / loops * 1000,
                2,
            )

            if not part_two:
                part_two = 'Not done'

            _cprint(f'\tPart Two: {part_two} ({part_two_time}ms)', OKGREEN)


def generate() -> None:
    """Generate a new solution file."""
    args = sys.argv[1:]

    if len(args) < 1:
        _cprint('Specify a solution date in the format "YYYY:DD"', FAIL)
        sys.exit(1)

    solution = args[0]

    if not re.match(r'\d{4}:\d{2}', solution):
        _cprint(f'{solution} is not a valid format, use YYYY:DD', FAIL)
        sys.exit(1)

    year, day = solution.split(':')
    short_day = day.removeprefix('0')
    folder = f'app/y{year}'

    response = requests.get(AOC_WEB.format(
        year=year,
        day=short_day,
    ))
    match = re.search(r'<h2>--- Day \d{1,2}:(.*)---</h2>', response.text)

    if not match:
        _cprint(f'Error downloading solution {solution}!', FAIL)
        sys.exit(1)

    raw_name = html.unescape(match.group(1).strip())
    name = re.sub(
        r'[^\w]', '',
        raw_name.lower().replace(' ', '_').replace('-', '_'),
    )
    solution_file = Path(f'{folder}/d{day}_{name}.py')

    if solution_file.exists():
        _cprint(f'There is already a solution for {solution}!', FAIL)
        sys.exit(1)

    with open('resources/template.py', 'r') as handle:
        template = handle.read().replace(
            '_YEAR_', year,
        ).replace(
            '_SHORT_DAY_', short_day,
        ).replace(
            '_DAY_', day,
        ).replace(
            '_NAME_', raw_name,
        )

    try:
        os.mkdir(folder)

        with open(f'{folder}/__init__.py', 'w') as handle:
            handle.write(f'"""Solvers for {year}."""\n')
    except FileExistsError:
        pass

    os.makedirs(f'input/{year}/{day}', exist_ok=True)

    with open(solution_file, 'w') as handle:
        handle.write(template)

    _cprint(f'Created {solution_file}!', OKGREEN)


def _cprint(text: str, color: str = None) -> None:
    if not color:
        color = ''

    print(f'{color}{text}{ENDC}')  # noqa: T001
