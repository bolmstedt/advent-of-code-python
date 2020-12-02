"""Automatic tests for Advent of Code solutions."""
from typing import List, Union

import pytest

from app import utils
from app.base_solver import BaseSolver
from tests import register

SOLVERS = utils.load_solvers()


@pytest.mark.parametrize('year,day,data,expected', [
    [year, day, test['data'], test['expected']]
    for year, days in register.TESTS.items()
    for day, tests in days.items()
    for test in tests
])
def test_days(
    year: str,
    day: str,
    data: str,
    expected: List[Union[int, str, None]],
) -> None:
    """Tests solvers."""
    try:
        solver: BaseSolver = SOLVERS[year][day]
    except KeyError:
        pytest.skip(f'There is no solver for {year}:{day}')

        return

    if expected[0] is None and expected[1] is None:
        pytest.skip('No expected results')

        return

    with open(f'input/{solver.year}/{solver.day}/{data}.txt', 'r') as handle:
        data = handle.read().strip()

    if expected[0] is not None:
        assert solver.part_one(data) == expected[0]

    if expected[1] is not None:
        assert solver.part_two(data) == expected[1]
