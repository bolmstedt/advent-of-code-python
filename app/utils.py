"""Various helper utils."""
import glob
import importlib
from typing import Iterable

from app.base_solver import BaseSolver

APP_PATH = 'app'


def load_solvers() -> Iterable[BaseSolver]:
    """Load all day solvers."""
    for year_path in glob.glob(f'{APP_PATH}/y*'):
        year = year_path.removeprefix(f'{APP_PATH}/')

        for day_module in glob.glob(f'{APP_PATH}/{year}/d*'):
            day_module_name = day_module.removeprefix(
                f'{APP_PATH}/{year}/',
            ).removesuffix('.py')
            solver = importlib.import_module(
                f'{APP_PATH}.{year}.{day_module_name}',
            )

            if hasattr(solver, 'Solver'):
                yield solver.Solver()  # type: ignore[attr-defined]
