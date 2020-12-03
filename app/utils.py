"""Various helper utils."""
import glob
import importlib
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
