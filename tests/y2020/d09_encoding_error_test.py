"""Custom tests for day 09, 2020."""
from app import utils
from app.y2020.d09_encoding_error import Solver
from tests.register import EXAMPLE


def test_part_one_example() -> None:
    """Test solver for part one."""
    solver = Solver()
    data = utils.load_input(solver, EXAMPLE)
    assert solver._solve_part_one(solver._parse_int_lines(data), 5) == 127


def test_part_two_example() -> None:
    """Test solver for part two."""
    solver = Solver()
    data = utils.load_input(solver, EXAMPLE)
    assert solver._solve_part_two(solver._parse_int_lines(data), 127) == 62
