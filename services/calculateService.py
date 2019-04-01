from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from config import *


def calculateConcentrationsLines(systemObj, constants, timeInterval):
    initialConcentrations = []
    for reagentName in systemObj['reagentsList']:
        configVal = CALCULATION_CONFIG['INITIAL_CONCENTRATIONS'][reagentName]
        initialConcentrations.append(configVal)

    tAxis = np.linspace(timeInterval[0],
                        timeInterval[1], CALCULATION_CONFIG['INTEGRATION_INTERVAL'])

    def pend(y, tAxis, concentrationsSigns, equations, constants):

        # assign C_A,C_B ... C_n to values from initial concentrations array
        for i in range(0, len(concentrationsSigns)):
            globals()[concentrationsSigns[i]] = y[i]

        # assign k1,k2...kn to values from constants array
        for i in range(0, len(constants)):
            globals()['k'+str(i+1)] = constants[i]

        return [eval(equations[0]), eval(equations[1]), eval(equations[2]), eval(equations[3])]

    concentrationsSigns = systemObj['concentrationsSigns']
    equations = systemObj['system']

    sol = odeint(pend, initialConcentrations, tAxis, args=(
        concentrationsSigns, equations, constants))

    return sol


def getCalculationsSetByVariants(systemObj, constantsPopulation):

    result = []
    # for constantsSet in constantsSet:
    #     obj = {}
    #     obj['constantsSet'] = constantsSet
    #     obj['concentrations'] = []
    #     for timeValue in range(CALCULATION_CONFIG['TIME_INTERVAL'][0], CALCULATION_CONFIG['TIME_INTERVAL'][1], CALCULATION_CONFIG['STEP_TO_DIVIDE']):
    #         subTimeIntervalObj = {}
    #         subTimeIntervalObj['timeInterval'] = [
    #             timeValue, timeValue+CALCULATION_CONFIG['STEP_TO_DIVIDE']]
    #         subTimeIntervalObj['concentrationsVsTime'] = calculateConcentrationsLines(systemObj,constantsSet,subTimeIntervalObj['timeInterval'])
    #         obj['concentrations'].append(subTimeIntervalObj.copy())

    #     result.append(obj)

    for timeValue in range(CALCULATION_CONFIG['TIME_INTERVAL'][0], CALCULATION_CONFIG['TIME_INTERVAL'][1], CALCULATION_CONFIG['STEP_TO_DIVIDE']):
        obj = {}
        obj['timeInterval'] = [
                timeValue, timeValue+CALCULATION_CONFIG['STEP_TO_DIVIDE']]
        obj['data'] = []
        for constantsSet in constantsPopulation:
            subTimeIntervalObj = {}
            subTimeIntervalObj['constantsSet'] = constantsSet
            subTimeIntervalObj['concentrationLine'] = calculateConcentrationsLines(systemObj,constantsSet,obj['timeInterval'])
            obj['data'].append(subTimeIntervalObj.copy())

        result.append(obj)

    

    return result
