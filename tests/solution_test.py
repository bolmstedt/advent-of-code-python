"""Automatic tests for Advent of Code solutions."""
from typing import Union

import pytest

from app import utils
from app.base_solver import BaseSolver
from tests import register

SOLVERS = utils.load_solvers()
INPUT_PATH = 'input/{solver.year}/{solver.day}/{data}.txt'


@pytest.mark.parametrize('year,day,data,one,two', [
    [year, day, data, test.get('one'), test.get('two')]
    for year, days in register.TESTS.items()
    for day, tests in days.items()
    for test in tests
    for data in test['data']
])
def test_days(
    year: str,
    day: str,
    data: str,
    one: Union[int, str, None],
    two: Union[int, str, None],
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

    if one is None and two is None:
        pytest.skip('No expected results')

        return

    if data in [register.EXAMPLE, register.INPUT]:
        with open(
            f'input/{solver.year}/{solver.day}/{data}.txt', 'r',
        ) as handle:
            data = handle.read().strip()

    if one is not None:
        assert solver.part_one(data) == one

    if two is not None:
        assert solver.part_two(data) == two
