from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

INTEGRATION_INTERVAL = 5


def calculateConcentrationsLines(k1, k2, k3):
    def pend(y, t, k1, k2, k3):
        ca, cb, cc, cd = y
        dydt = [3*(-k1*(ca**3) + k2*(cb**2)),
                2*(k1*(ca**3)-k2*(cb**2) - k3*cb*(cc**2)),
                (-2)*k3*cb*(cc**2),
                k3*cb*(cc**2)
                ]
        return dydt

    y0 = [6, 0, 8, 0]

    t = np.linspace(0, 5, INTEGRATION_INTERVAL)

    sol = odeint(pend, y0, t, args=(k1, k2, k3))

    return sol


def getCalculationsSetByVariants(constantsSet):
    result = []
    for constantsSet in constantsSet:
        obj = {}
        obj['constantsSet'] = constantsSet
        obj['concentrationsLine'] = calculateConcentrationsLines(
            *constantsSet)
        result.append(obj)

    return result