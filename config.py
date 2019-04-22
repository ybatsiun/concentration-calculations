#TODO caps
constants = [
    {
        'min': 1,
        'max': 5,
        'step': 1
    },
    {
        'min':32,
        'max':40,
        'step':1
    },
    {
        'min':100,
        'max':190,
        'step':1
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'INTEGRATION_INTERVAL': 16,
    'TIME_INTERVAL': [0, 10],
    'STEP_TO_DIVIDE': 5,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0,"C": 8, "D": 0}
}

# TODO dimension converting for data to a separate method
# move data validation to FE form validation
# might need to split python module to different task(getEquations - now can validate constant amount,concentrations amount
# - and other functions)
# TODO handle on FE
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?