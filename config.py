constants = [
    {
        'min': 1,
        'max': 30,
        'step': 1
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A->2B"],
    'INTEGRATION_INTERVAL': 50,
    'TIME_INTERVAL': [0, 1],
    'STEP_TO_DIVIDE': 1,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0}
}

# TODO
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?
# write ready objects to .json to prevent big data being kept in a memory
