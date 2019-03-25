constants = [
    {
        'min': 1,
        'max': 30,
        'step': 5
    },
    {
        'min': 4,
        'max': 6,
        'step': 1,
    },
    {
        'min': 0,
        'max': 8,
        'step': 2,
    }
]

calculation = {
    'equations': ["3A=2B", "B+2C->D"],
    'INTEGRATION_INTERVAL': 1000,
    'TIME_INTERVAL': [0, 8],
    'STEP_TO_DIVIDE': 4,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0, "C": 8, "D": 0}
}

# TODO
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?
# write ready objects to .json to prevent big data being kept in a memory
