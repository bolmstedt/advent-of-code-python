"""Solution for day 4, 2020."""
import re
from typing import Dict, List, Union

from app.base_solver import BaseSolver

FIELD = re.compile(r'\w+:[\w#]+')
HEX_VALUE = re.compile(r'^#[a-f0-9]{6}$')
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
NINE_DIGITS = re.compile(r'^[0-9]{9}$')
PassportType = Dict[str, str]


REQUIRED = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'ecl': lambda v: v in EYE_COLORS,
    'hcl': lambda v: HEX_VALUE.search(v) is not None,
    'pid': lambda v: NINE_DIGITS.search(v) is not None,
    'hgt': lambda v: (
        (v.endswith('cm') and 150 <= int(v[:-2]) <= 193) or
        (v.endswith('in') and 59 <= int(v[:-2]) <= 76)
    ),
}


class Solver(BaseSolver):
    """Solver for day 4, 2020."""

    day = '04'
    year = '2020'
    name = r"""Passport Processing"""

    def part_one(self, data: str) -> Union[int, str]:
        """Solve part one."""
        return sum(
            all(r in passport for r in REQUIRED)
            for passport in self._parse_input(data)
        )

    def part_two(self, data: str) -> Union[int, str]:
        """Solve part two."""
        return sum(
            self._valid_fields(passport)
            for passport in self._parse_input(data)
        )

    @staticmethod
    def _valid_fields(passport: PassportType) -> bool:
        for field, validator in REQUIRED.items():
            if field not in passport or not validator(passport.get(field)):
                return False

        return True

    @staticmethod
    def _parse_input(data: str) -> List[PassportType]:
        passports = []

        for passport in data.split('\n\n'):
            matches = FIELD.findall(passport)

            if not matches:
                continue

            passports.append(
                {k: v for k, v in [group.split(':') for group in matches]},
            )

        return passports
