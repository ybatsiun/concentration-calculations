import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService
import services.mlService
from config import *
import time

# TODO move it to another file to make a separate task
systemObj = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

start = time.time()
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
print(time.time() - start)
networks = services.mlService.getTrainNetworks(results)
# predict
experimentalData = fsService.readJsonFile('input.json')

#services.fsService.writeJsonToFile(results,'results.json')
#print(results)