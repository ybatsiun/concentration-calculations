#TODO caps
constants = [
    {
        'min': 2,
        'max': 3,
        'step': 1
    },
    {
        'min':0.5,
        'max':1,
        'step':0.5
    },
    {
        'min':1,
        'max':2,
        'step':1
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'INTEGRATION_INTERVAL': 700,
    'TIME_INTERVAL': [0, 5],
    'STEP_TO_DIVIDE': 5,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0,"C": 8, "D": 0}
}

# move data validation to FE form validation
# might need to split python module to different task(getEquations - now can validate constant amount,concentrations amount
# - and other functions)
# TODO handle on FE
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?