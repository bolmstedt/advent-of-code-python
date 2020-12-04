"""Automatic tests for Advent of Code solutions."""
from typing import Union

import pytest

from app import utils
from app.base_solver import BaseSolver
from tests import register

SOLVERS = utils.load_solvers()
INPUT_PATH = 'input/{solver.year}/{solver.day}/{data}.txt'


@pytest.mark.parametrize('year,day,part,data,expected', [
    [year, day, part, data, test.get(part)]
    for year, days in register.TESTS.items()
    for day, tests in days.items()
    for test in tests
    for data in test['data']
    for part in ['one', 'two']
    if test.get(part)
])
def test_days(
    year: str,
    day: str,
    part: str,
    data: str,
    expected: Union[int, str],
    full: bool,
    solution: str,
) -> None:
    """Tests solvers."""
    if solution != 'all' and solution != f'{year}:{day}':
        pytest.skip(f'Skipping solvers other than {solution}')

        return

    if not full and data == register.INPUT:
        pytest.skip('Full solutions need --full option to run')

        return

    try:
        solver: BaseSolver = SOLVERS[year][day]
    except KeyError:
        pytest.skip(f'There is no solver for {year}:{day}')

        return

    if expected is None:
        pytest.skip('No expected results')

        return

    if data == register.INPUT or data.startswith(register.EXAMPLE):
        with open(
            f'input/{solver.year}/{solver.day}/{data}.txt', 'r',
        ) as handle:
            data = handle.read().strip()

    method = getattr(solver, f'part_{part}')
    assert method(data) == expected
