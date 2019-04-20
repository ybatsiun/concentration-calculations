import services.calculateService
import services.variationService
import services.fsService
import services.parsingService
import services.mlService
from config import *
import time

systemObj = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
services.mlService.getTrainNetworks(results)

#services.fsService.writeJsonToFile(results,'test.json')
#print(results)