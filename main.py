import calculateService
import variationService
import fsService
from config import *


constantsVariations = variationService.getVariants(constants)
results = calculateService.getCalculationsSetByVariants(constantsVariations)
fsService.writeToFile(results,'test.json')
