import calculateService
import variationService
import fsService
import parsingService
from config import *


systemObj = parsingService.getEquations()
constantsVariations = variationService.getVariants(constants)
results = calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
print(results)
fsService.writeToFile(results,'test.json')


