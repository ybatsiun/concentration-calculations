import calculateService
import variationService
import fsService
import parsingService
from config import *


# constantsVariations = variationService.getVariants(constants)
# results = calculateService.getCalculationsSetByVariants(constantsVariations)
# fsService.writeToFile(results,'test.json')

x = parsingService.getEquations()

print(x)
