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
# inputFilePath = sys.argv[1]
# experimentalData = fsService.readJsonFile(inputFilePath)
experimentalData = eval(sys.argv[1])
config = eval(sys.argv[2])
partsToDivide = config['calculationConfig']['partsToDivide']
equationDataArray = eval(sys.argv[3])

intregrationInterval = len(experimentalData)
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(
    experimentalData, partsToDivide)

# parse user's input: system of chemical equations
# equationDataArray = parsingService.getEquations(
#     CALCULATION_CONFIG['equations'])
equationData = parsingService.convertEquations(equationDataArray)
constantsVariations = services.variationService.getVariants(
    config['speedConstants'])

timeInterval = config['calculationConfig']['timeInterval']
results = services.calculateService.getCalculationsSetByVariants(
    equationData, constantsVariations, intregrationInterval, timeInterval, partsToDivide, config['calculationConfig']['initialConcentrations'])
networks = mlService.getTrainNetworks(results)

predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

metricsService.getRelativeError(predictions)

#fsService.writeJsonToFile(results, 'server/machineLearningModule/results.json')
log('process was ended successfully')
