"""Various helper utils."""
import glob
import importlib
import pathlib
from typing import Dict

from app.base_solver import BaseSolver


def load_solvers() -> Dict[str, Dict[str, BaseSolver]]:
    """Load all day solvers."""
    solvers: Dict[str, Dict[str, BaseSolver]] = {}

    for year_path in sorted(glob.glob('app/y*')):
        year = year_path.removeprefix('app/')

        for day_path in sorted(glob.glob(f'{year_path}/d*')):
            day_module = day_path.removeprefix(
                f'{year_path}/',
            ).removesuffix('.py')
            module = importlib.import_module(
                f'app.{year}.{day_module}',
            )

            if hasattr(module, 'Solver'):
                solver = module.Solver()  # type: ignore[attr-defined]

                if solver.year not in solvers:
                    solvers[solver.year] = {}

                solvers[solver.year][solver.day] = solver

    return solvers


def load_input(solver: BaseSolver, data: str) -> str:
    """Load the input for a solver."""
    data_file = pathlib.Path(f'input/{solver.year}/{solver.day}/{data}.txt')

    if not data_file.is_file():
        raise FileNotFoundError(f'{data_file.name} does not exist!')

    with open(data_file, 'r') as handle:
        return handle.read().strip()
