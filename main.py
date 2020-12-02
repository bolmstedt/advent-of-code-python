"""Advent of Code solutions."""
import sys
import time

from app import utils


def _main(only: str = None) -> None:
    solvers = utils.load_solvers()

    for solver in solvers:
        if only and f'{solver.year}:{solver.day}' != only:
            continue

        with open(
            f'input/{solver.year}/{solver.day}/input.txt',
            'r',
        ) as handle:
            data = handle.read().strip()

        start = time.perf_counter()
        part_one = solver.part_one(data)
        part_one_time = round((time.perf_counter() - start) * 1000, 2)

        start = time.perf_counter()
        part_two = solver.part_two(data)
        part_two_time = round((time.perf_counter() - start) * 1000, 2)

        print(solver.full_name)  # noqa: T001
        print(f'\tPart One: {part_one} ({part_one_time}ms)')  # noqa: T001
        print(f'\tPart Two: {part_two} ({part_two_time}ms)')  # noqa: T001

    exit()


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0:
        _main()

    _main(args[0])
