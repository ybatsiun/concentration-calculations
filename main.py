import system
import variate
from config import *


constantsVariations = variate.getVariants(constants)

result = []
for constantsSet in constantsVariations:
    obj = {}
    obj['constantsSet'] = constantsSet
    obj['concentrationsLine'] = system.calculateConcentrationsLines(
        *constantsSet)
    result.append(obj)
