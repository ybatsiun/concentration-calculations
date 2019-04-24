from config import *
import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService
import services.mlService as mlService
import services.metricsService as metricsService
import services.utilsService as utils
from services.loggerService import log
import time
import numpy as np
import sys

log('started the process')

# get experimental data
inputFilePath = sys.argv[1]
experimentalData = fsService.readJsonFile(inputFilePath)
intregrationInterval = len(experimentalData)
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(experimentalData)

# TODO move it to another file to make a separate task
equationData = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(SPEED_CONSTANTS)

results = services.calculateService.getCalculationsSetByVariants(
    equationData, constantsVariations,intregrationInterval)
networks = mlService.getTrainNetworks(results)



predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

metricsService.getRelativeError(predictions)

fsService.writeJsonToFile(results, 'results.json')

log('process was ended successfully')