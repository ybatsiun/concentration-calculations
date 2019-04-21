#TODO caps
constants = [
    {
        'min': 1,
        'max': 20,
        'step': 1
    },
    {
        'min':30,
        'max':50,
        'step':2
    },
    {
        'min':100,
        'max':900,
        'step':50
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'INTEGRATION_INTERVAL': 15,
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