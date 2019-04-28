SPEED_CONSTANTS = [
    {
        'min': 5,
        'max': 15,
        'step': 5
    },
    {
        'min':10,
        'max':20,
        'step':5
    },
    {
        'min':30,
        'max':50,
        'step':5
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'TIME_INTERVAL': [0, 15],
    'PARTS_TO_DIVIDE': 3,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0,"C": 8, "D": 0},
}

# move data validation to FE form validation
# might need to split python module to different task(getEquations - now can validate constant amount,concentrations amount
# - and other functions)
# TODO handle on FE
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?