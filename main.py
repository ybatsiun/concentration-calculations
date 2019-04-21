import services.calculateService
import services.variationService
import services.fsService as fsService
import services.parsingService
import services.mlService
from config import *
import time
import numpy as np

# TODO move it to another file to make a separate task
systemObj = services.parsingService.parseEquations(CALCULATION_CONFIG['equations'])
constantsVariations = services.variationService.getVariants(constants)

start = time.time()
results = services.calculateService.getCalculationsSetByVariants(systemObj,constantsVariations)
print(time.time() - start)
networks = services.mlService.getTrainNetworks(results)
#experimentalData = fsService.readJsonFile('input.json')
experimentalData1 = fsService.readJsonFile('results.1.json')['0.5x16_2/35/110_corrupted']
experimentalData2 = fsService.readJsonFile('results.1.json')['5.10x16_2/35/110']
experimentalData3 = fsService.readJsonFile('results.1.json')['10.15x16_4x35x210']

# convert to 2d
dataset_size = len([experimentalData1])
experimentalData_2d_1 = np.asarray(experimentalData1).reshape(dataset_size,-1)
experimentalData_2d_2 = np.asarray(experimentalData2).reshape(dataset_size,-1)
experimentalData_2d_3 = np.asarray(experimentalData3).reshape(dataset_size,-1)

pr = networks[0].predict(experimentalData_2d_1)
print('prediction1')
print(pr)

pr = networks[0].predict(experimentalData_2d_2)
print('prediction2')
print(pr)

pr = networks[0].predict(experimentalData_2d_3)
print('prediction3')
print(pr)

fsService.writeJsonToFile(results,'results.json')