from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from config import *
import services.fsService


def getConcentrationsLines(equationDataArray, constants, timeInterval):
    """
        Calculates and return concentration lines(concentration of reagent vs. time)

        Parameters:
        equationdataArray (Array): Array of objects each containing sign of reagent(A,B...), function to get the value of dC(A,B...)
        constants (array): 2d-array. Each item contains a unique set of speed constants for the chemical process
        timeInterval (array): start and finish of a chemical process takes place. Aribitrary units 
    """

    def pend(y, tAxis, equationDataArray, constants):
        args = {}
        # assign k1,k2...kn to values from constants array
        for i in range(0, len(constants)):
            args["k" + str(i + 1)] = constants[i]

        for i in range(0, len(equationDataArray)):
            # assign C_A,C_B ... C_n to values from initial concentrations array
            concentrationSign =  "C_{}".format(equationDataArray[i]['reagent'])
            args[concentrationSign] = y[i]

        equationsValues = []
        for equationData in equationDataArray:
            equationsValues.append(equationData['function'](args))
        return equationsValues

    initialConcentrations = []
    for equationData in equationDataArray:
        configVal = CALCULATION_CONFIG["INITIAL_CONCENTRATIONS"][equationData['reagent']]
        initialConcentrations.append(configVal)

    tAxis = np.linspace(
        timeInterval[0], timeInterval[1], CALCULATION_CONFIG["INTEGRATION_INTERVAL"])
    
    sol = odeint(
        pend,
        initialConcentrations,
        tAxis,
        args=(equationDataArray, constants))

    return sol


def getCalculationsSetByVariants(systemObj, constantsPopulation):

    result = []

    for timeValue in range(
        CALCULATION_CONFIG["TIME_INTERVAL"][0],
        CALCULATION_CONFIG["TIME_INTERVAL"][1],
        CALCULATION_CONFIG["STEP_TO_DIVIDE"],
    ):
        obj = {}
        obj["timeInterval"] = [
            timeValue,
            timeValue + CALCULATION_CONFIG["STEP_TO_DIVIDE"],
        ]
        obj["data"] = []
        for constantsSet in constantsPopulation:
            subTimeIntervalObj = {}
            subTimeIntervalObj["constantsSet"] = constantsSet
            subTimeIntervalObj["concentrationLine"] = getConcentrationsLines(
                systemObj, constantsSet, obj["timeInterval"]
            ).tolist()
            obj["data"].append(subTimeIntervalObj.copy())

        result.append(obj)
        # services.fsService.writeJsonToFile(obj,'results.json')

    return result
