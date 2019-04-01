import services.calculateService
import services.variationService
import services.fsService
import services.parsingService
from config import *


systemObj = services.parsingService.getEquations()
constantsVariations = services.variationService.getVariants(constants)
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)

services.fsService.writeToFile(results,'test.json')

print(results)