#TODO caps
constants = [
    {
        'min': 1,
        'max': 20,
        'step': 1
    },
    {
        'min':50,
        'max':60,
        'step':1
    },
    {
        'min':90,
        'max':100,
        'step':1
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'INTEGRATION_INTERVAL': 70,
    'TIME_INTERVAL': [0, 5],
    'STEP_TO_DIVIDE': 5,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 1,"C": 8, "D": 0}
}

# TODO
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?
# write ready objects to .json to prevent big data being kept in a memory
