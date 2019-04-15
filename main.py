import services.calculateService
import services.variationService
import services.fsService
import services.parsingService
import services.mlService
from config import *


systemObj = services.parsingService.getEquations()
constantsVariations = services.variationService.getVariants(constants)
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
services.mlService.getTrainNetworks(results)
services.fsService.writeJsonToFile(results,'test.json')

#print(results)