"""Automatic tests for Advent of Code solutions."""
from typing import List, Union

import pytest

from app import utils
from app.base_solver import BaseSolver
from tests import register

SOLVERS = utils.load_solvers()
INPUT_PATH = 'input/{solver.year}/{solver.day}/{data}.txt'


@pytest.mark.parametrize('year,day,data,one,two', [
    [year, day, test['data'], test.get('one'), test.get('two')]
    for year, days in register.TESTS.items()
    for day, tests in days.items()
    for test in tests
])
def test_days(
    year: str,
    day: str,
    data: Union[str, List[str]],
    one: Union[int, str, None],
    two: Union[int, str, None],
) -> None:
    """Tests solvers."""
    try:
        solver: BaseSolver = SOLVERS[year][day]
    except KeyError:
        pytest.skip(f'There is no solver for {year}:{day}')

        return

    if one is None and two is None:
        pytest.skip('No expected results')

        return

    if isinstance(data, str):
        with open(
            f'input/{solver.year}/{solver.day}/{data}.txt', 'r',
        ) as handle:
            data = [handle.read().strip()]

    for input_data in data:
        if one is not None:
            assert solver.part_one(input_data) == one

        if two is not None:
            assert solver.part_two(input_data) == two
