import services.calculateService
import services.variationService
import services.fsService
import services.parsingService
import services.mlService
from config import *
import time

systemObj = services.parsingService.getEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

start = time.time()
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
end = time.time()
print(end - start)
#services.mlService.getTrainNetworks(results)

#services.fsService.writeJsonToFile(results,'test.json')
