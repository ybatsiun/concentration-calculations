import demjson
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
import time

log('started the process')
start = time.time()

experimentalData = eval(sys.argv[1])
config = eval(sys.argv[2])
partsToDivide = config['calculationConfig']['partsToDivide']
equationDataArray = eval(sys.argv[3])
log('parsed')

intregrationInterval = len(experimentalData)
log('intergration interval' + str(intregrationInterval))
experimentalDataByTimeInterval = utils.splitConcentrationsByTimeInterval(
    experimentalData, partsToDivide)


equationData = parsingService.convertEquations(equationDataArray, len(config['speedConstants']) )
constantsVariations = services.variationService.getVariants(
    config['speedConstants'])


timeInterval = config['calculationConfig']['timeInterval']
results = services.calculateService.getCalculationsSetByVariants(
    equationData, constantsVariations, intregrationInterval, timeInterval, partsToDivide, config['calculationConfig']['initialConcentrations'])
fsService.writeJsonToFile(results, 'results.json')
networks = mlService.getTrainNetworks(results)

predictions = mlService.getPredictionsArray(
    networks, experimentalDataByTimeInterval)

metricsService.getRelativeError(predictions)

end = time.time()
log('process was ended successfully')
log('Time of execution: ' + str(round(end - start,1)) + ' seconds',True)
