from config import *
import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService
import services.mlService as mlService
import services.metricsService as metricsService
import services.utilsService as utils
import time
import numpy as np

# TODO move it to another file to make a separate task
systemObj = services.parsingService.parseEquations(
    CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

start = time.time()
results = services.calculateService.getCalculationsSetByVariants(
    systemObj, constantsVariations)
print(time.time() - start)
networks = mlService.getTrainNetworks(results)
# get experimental data
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(
    fsService.readJsonFile(CALCULATION_CONFIG['INPUT_FILE_PATH'])
)


predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

print(predictions)
metricsService.getRelativeError(predictions)

fsService.writeJsonToFile(results, 'results.json')
