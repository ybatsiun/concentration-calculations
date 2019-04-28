from config import *
from services.loggerService import log
import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService as parsingService
import services.mlService as mlService
import services.metricsService as metricsService
import services.utilsService as utils
import numpy as np
import sys

log('started the process')

# get experimental data
inputFilePath = sys.argv[1]
experimentalData = fsService.readJsonFile(inputFilePath)
intregrationInterval = len(experimentalData)
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(experimentalData)

# parse user's input: system of chemical equations
equationDataArray = parsingService.getEquations(CALCULATION_CONFIG['equations'])
equationData = parsingService.convertEquations(equationDataArray)
constantsVariations = services.variationService.getVariants(SPEED_CONSTANTS)

results = services.calculateService.getCalculationsSetByVariants(
    equationData, constantsVariations,intregrationInterval)
networks = mlService.getTrainNetworks(results)

predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

metricsService.getRelativeError(predictions)

fsService.writeJsonToFile(results, 'results.json')

log('process was ended successfully')