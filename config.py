SPEED_CONSTANTS = [
    {
        'min': 1,
        'max': 2,
        'step': 1
    },
    {
        'min':36,
        'max':39,
        'step':1
    },
    {
        'min':110,
        'max':120,
        'step':1
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'INTEGRATION_INTERVAL': 32,
    'TIME_INTERVAL': [0, 10],
    'PARTS_TO_DIVIDE': 2,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0,"C": 8, "D": 0},
    'INPUT_FILE_PATH': 'input.json'
}

# move data validation to FE form validation
# might need to split python module to different task(getEquations - now can validate constant amount,concentrations amount
# - and other functions)
# TODO handle on FE
# amount of constants != to constants in equations
# amount initial concentrations != reagents

# what constans is to what equation?