`input.json` contains 'experimental' data of concentration changes
* time period: [0,10]
* constants: [3,36,110]
* chemical equations: ["3A=2B","B+2C->D"]
* parts to divide: `2`
* number of 'experimental observations' i.e. `integration interval`: 32

Run this file to obtain results with constants range containing values from constants above and with chemical equations above.
Example of `config.js` to run this `input.js`:
```javascript
SPEED_CONSTANTS = [
    {
        'min': 1,
        'max': 6,
        'step': 1
    },
    {
        'min':26,
        'max':48,
        'step':2
    },
    {
        'min':70,
        'max':160,
        'step':5
    }
]

CALCULATION_CONFIG = {
    'equations': ["3A=2B","B+2C->D"],
    'TIME_INTERVAL': [0, 10],
    'PARTS_TO_DIVIDE': 2,
    'INITIAL_CONCENTRATIONS': {"A": 6, "B": 0,"C": 8, "D": 0},
}
```

Example output:
```
predictions:
[  3. ,  36.1, 110.4], [  3.  ,  36.24, 110.25]
relative error per answer in percent
[0.        , 0.19353055, 0.06798097],[0.        , 0.19353055, 0.06798097]
```
Variate with equations, constant range and step to obtain different results