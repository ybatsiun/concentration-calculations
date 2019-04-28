from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from config import *
import services.fsService
import services.utilsService as utils
from services.loggerService import log


def getConcentrationsLines(equationDataArray, constants, timeInterval, intregrationInterval, initialConcentrations):
    """
        Calculates and return concentration lines(concentration of reagent vs. time)

        Parameters:
        equationdataArray (Array): Array of objects each containing sign of reagent(A,B...), function to get the value of dC(A,B...)
        constants (array): 2d-array. Each item contains a unique set of speed constants for the chemical process
        timeInterval (array): start and finish of a chemical process takes place. Aribitrary units
        integrationInterval: amount of points on concentration axis
    """

    def pend(y, tAxis, equationDataArray, constants):
        args = {}
        # assign k1,k2...kn to values from constants array
        for i in range(0, len(constants)):
            args["k" + str(i + 1)] = constants[i]

        for i in range(0, len(equationDataArray)):
            # assign C_A,C_B ... C_n to values from initial concentrations array
            concentrationSign = "C_{}".format(equationDataArray[i]['reagent'])
            args[concentrationSign] = y[i]

        equationsValues = []
        for equationData in equationDataArray:
            # get function value and convert to <float>
            equationsValues.append(equationData['function'](args).item())
        return equationsValues

    initialConcentrationsValues = []
    for equationData in equationDataArray:
        configVal = initialConcentrations[equationData['reagent']]
        initialConcentrationsValues.append(configVal)

    tAxis = np.linspace(
        timeInterval[0], timeInterval[1], intregrationInterval)
    sol = odeint(
        pend,
        initialConcentrationsValues,
        tAxis,
        args=(equationDataArray, constants))

    return sol


def getCalculationsSetByVariants(equationData, constantsPopulation, intregrationInterval, timeInterval, partsToDivide, initialConcentrations):
    timeIntervalDivisionStep = int(timeInterval[1] / partsToDivide)
    result = []

    for timeValue in range(timeInterval[0], timeInterval[1], timeIntervalDivisionStep):
        result.append({'timeInterval': [
            timeValue,
            timeValue + timeIntervalDivisionStep], "data": []})

    for constantsSet in constantsPopulation:

        concentrations = getConcentrationsLines(
            equationData, constantsSet, timeInterval, intregrationInterval, initialConcentrations).tolist()
        splittedConcentrations = utils.splitConcentrationsByTimeInterval(
            concentrations, partsToDivide)

        # collect in object
        for i in range(0, len(splittedConcentrations)):
            obj = {"constantsSet": constantsSet,
                   "concentrationLine": splittedConcentrations[i]}
            result[i]['data'].append(obj)

    log('data for neural networks training were generated')
    return result
