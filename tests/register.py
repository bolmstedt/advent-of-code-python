"""A register of test data for solvers."""
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
                'data': 'input',
                'one': 138,
                'two': 1771,
            },
        ],
    },
    '2019': {
        '01': [
            {
                'data': 'example',
                'one': 34241,
                'two': 51316,
            },
            {
                'data': 'input',
                'one': 3282935,
                'two': 4921542,
            },
        ],
    },
    '2020': {
        '01': [
            {
                'data': 'example',
                'one': 514579,
                'two': 241861950,
            },
            {
                'data': 'input',
                'one': 982464,
                'two': 162292410,
            },
        ],
        '02': [
            {
                'data': 'example',
                'one': 2,
                'two': 1,
            },
            {
                'data': 'input',
                'one': 396,
                'two': 428,
            },
        ],
    },
}
