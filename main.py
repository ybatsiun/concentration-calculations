import calculateService
import variationService
from config import *


constantsVariations = variationService.getVariants(constants)

x = calculateService.getCalculationsSetByVariants(constantsVariations)
print(x)