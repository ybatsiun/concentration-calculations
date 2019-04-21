import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService
import services.mlService as mlService
from config import *
import time
import numpy as np

# TODO move it to another file to make a separate task
systemObj = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

start = time.time()
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
print(time.time() - start)
networks = mlService.getTrainNetworks(results)
# get experimental data
experimentalData = fsService.readJsonFile('input.json')

# convert to 2d
dataset_size = len([experimentalData[0]])
experimentalData_2d_1 = np.asarray(experimentalData[0]).reshape(dataset_size,-1)
experimentalData_2d_2 = np.asarray(experimentalData[1]).reshape(dataset_size,-1)
experimentalData_2d_3 = np.asarray(experimentalData[2]).reshape(dataset_size,-1)

predictions = mlService.getPredictionsArray(networks,[experimentalData_2d_1,experimentalData_2d_2,experimentalData_2d_3])

print(predictions)

fsService.writeJsonToFile(results,'results.json')