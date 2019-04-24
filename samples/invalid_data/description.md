`input.json` contains 'experimental' data of concentration changes
* time period: [0,5]
* constants: [14,26,70]
* time period: [5,10]
* constants: [7,41,99]
* chemical equations: ["3A=2B","B+2C->D"]
* parts to divide: `2`
* number of 'experimental observations' i.e. `integration interval`: 32

Run this file to obtain results with constants range containing values from constants above and with chemical equations above.
Example of `config.js` to run this `input.js`:
```javascript
SPEED_CONSTANTS = [
    {
        'min': 6,
        'max': 15,
        'step': 1
    },
    {
        'min':20,
        'max':45,
        'step':2
    },
    {
        'min':65,
        'max':105,
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
[14.03, 26.42, 70.1 ], [ 6.95, 39.24, 99.35]
relative error per answer in percent
[33.74642517, 19.52482486, 17.26172912], [33.74642517, 19.52482486, 17.26172912]
```
Variate with equations, constant range and step to obtain different results