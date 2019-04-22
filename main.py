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

log('started the process')
# TODO move it to another file to make a separate task
equationData = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(SPEED_CONSTANTS)

results = services.calculateService.getCalculationsSetByVariants(
    equationData, constantsVariations)
networks = mlService.getTrainNetworks(results)

# get experimental data
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(
    fsService.readJsonFile(CALCULATION_CONFIG['INPUT_FILE_PATH']))

predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

metricsService.getRelativeError(predictions)

fsService.writeJsonToFile(results, 'results.json')

log('process was ended successfully')