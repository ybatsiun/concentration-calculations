from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from config import *


def calculateConcentrationsLines(systemObj, constants):
    initialConcentrations = []
    for reagentName in systemObj['reagentsList']:
        configVal = calculation['INITIAL_CONCENTRATIONS'][reagentName]
        initialConcentrations.append(configVal)

    tAxis = np.linspace(calculation['TIME_INTERVAL'][0],
                        calculation['TIME_INTERVAL'][1], calculation['INTEGRATION_INTERVAL'])

    def pend(y, tAxis, concentrationsSigns, equations, constants):

        # assign C_A,C_B ... C_n to values from initial concentrations array
        for i in range(0,len(concentrationsSigns)):
            globals()[concentrationsSigns[i]] = y[i]

        # assign k1,k2...kn to values from constants array
        for i in range(0, len(constants)):
            globals()['k'+str(i+1)] = constants[i]

        k = [eval(equations[0]), eval(equations[1]),eval(equations[2]), eval(equations[3])]
        return [eval(equations[0]), eval(equations[1]),eval(equations[2]), eval(equations[3])]

    concentrationsSigns = systemObj['concentrationsSigns']
    equations = systemObj['system']
    sol = odeint(pend, initialConcentrations, tAxis, args=(
        concentrationsSigns, equations, constants))

        
    # plt.plot(tAxis, sol[:, 0], 'b', label=systemObj['concentrationsSigns'][0])
    # plt.plot(tAxis, sol[:, 1], 'g', label=systemObj['concentrationsSigns'][1])
    # plt.plot(tAxis, sol[:, 2], 'r', label=systemObj['concentrationsSigns'][2])
    # plt.plot(tAxis, sol[:, 3], 'k', label=systemObj['concentrationsSigns'][3])
    # plt.legend(loc='best')
    # plt.xlabel('t')
    # plt.grid()
    # plt.show()   
    breakpoint()
    return sol


def getCalculationsSetByVariants(systemObj, constantsSet):

    result = []
    for constantsSet in constantsSet:
        obj = {}
        obj['constantsSet'] = constantsSet
        obj['concentrationsLine'] = calculateConcentrationsLines(
            systemObj, constantsSet)
        calculateConcentrationsLines(systemObj, constantsSet)
        result.append(obj)

    return result
