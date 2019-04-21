import services.calculateService
import services.variationService
import services.fsService
import services.parsingService
import services.mlService
from config import *
import time

# TODO move it to another file to make a separate task
systemObj = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
services.mlService.getTrainNetworks(results)
# predict

#services.fsService.writeJsonToFile(results,'test.json')
#print(results)