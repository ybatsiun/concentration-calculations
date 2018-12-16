constants = [
    {
        'min': 1,
        'avg': 2,
        'max': 3
    },
    {
        'min': 4,
        'avg': 5,
        'max': 6
    },
    {
        'min': 7,
        'avg': 8,
        'max': 9
    }
]

calculation = {
    'equations': ["3A=2B", "B+2C->D"],
    'INTEGRATION_INTERVAL': 10,
    'TIME_INTERVAL': [0, 6],
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0, "C": 8, "D": 0}
}

# TODO
# amount of constants != to constants in equations
# amount initial concentrations != reagents
