"""A register of test data for solvers."""
from typing import Dict, List, TypedDict, Union

INPUT = 'input'
EXAMPLE = 'example'


class TestCase(TypedDict, total=False):
    """Typed dict for test cases."""

    data: List[str]
    one: Union[int, str]
    two: Union[int, str]


TESTS: Dict[str, Dict[str, List[TestCase]]]
TESTS = {
    '2015': {
        '01': [
            {
                'data': ['(())', '()()'],
                'one': 0,
            },
            {
                'data': ['(((', '(()(()(', '))((((('],
                'one': 3,
            },
            {
                'data': ['())', '))('],
                'one': -1,
            },
            {
                'data': [')))', ')())())'],
                'one': -3,
            },
            {
                'data': [')'],
                'two': 1,
            },
            {
                'data': ['()())'],
                'two': 5,
            },
            {
                'data': [INPUT],
                'one': 138,
                'two': 1771,
            },
        ],
        '02': [
            {
                'data': ['2x3x4'],
                'one': 58,
                'two': 34,
            },
            {
                'data': ['1x1x10'],
                'one': 43,
                'two': 14,
            },
            {
                'data': [INPUT],
                'one': 1586300,
                'two': 3737498,
            },
        ],
        '03': [
            {
                'data': ['>'],
                'one': 2,
            },
            {
                'data': ['^>v<'],
                'one': 4,
                'two': 3,
            },
            {
                'data': ['^v^v^v^v^v'],
                'one': 2,
                'two': 11,
            },
            {
                'data': ['^v'],
                'two': 3,
            },
            {
                'data': [INPUT],
                'one': 2565,
                'two': 2639,
            },
        ],
        '04': [
            {
                'data': ['abcdef'],
                'one': 609043,
            },
            {
                'data': ['pqrstuv'],
                'one': 1048970,
            },
            {
                'data': [INPUT],
                'one': 346386,
                'two': 9958218,
            },
        ],
        '05': [
            {
                'data': ['ugknbfddgicrmopn', 'aaa'],
                'one': 1,
            },
            {
                'data': [
                    'jchzalrnumimnmhp',
                    'haegwjzuvuyypxyu',
                    'dvszwmarrgswjxmb',
                ],
                'one': 0,
            },
            {
                'data': ['qjhvhtzxzqqjkmpb', 'xxyxx'],
                'two': 1,
            },
            {
                'data': ['uurcxstgmygtbstg', 'ieodomkazucvgmuy'],
                'two': 0,
            },
            {
                'data': [INPUT],
                'one': 236,
                'two': 51,
            },
        ],
        '06': [
            {
                'data': [f'{EXAMPLE}_1'],
                'one': 997997,
            },
            {
                'data': [f'{EXAMPLE}_2'],
                'two': 2000003,
            },
            {
                'data': [INPUT],
                'one': 377891,
                'two': 14110788,
            },
        ],
    },
    '2019': {
        '01': [
            {
                'data': [EXAMPLE],
                'one': 34241,
                'two': 51316,
            },
            {
                'data': [INPUT],
                'one': 3282935,
                'two': 4921542,
            },
        ],
    },
    '2020': {
        '01': [
            {
                'data': [EXAMPLE],
                'one': 514579,
                'two': 241861950,
            },
            {
                'data': [INPUT],
                'one': 982464,
                'two': 162292410,
            },
        ],
        '02': [
            {
                'data': [EXAMPLE],
                'one': 2,
                'two': 1,
            },
            {
                'data': [INPUT],
                'one': 396,
                'two': 428,
            },
        ],
        '03': [
            {
                'data': [EXAMPLE],
                'one': 7,
                'two': 336,
            },
            {
                'data': [INPUT],
                'one': 218,
                'two': 3847183340,
            },
        ],
    },
}
