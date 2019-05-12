import numpy
from services.loggerService import log

def getVariants(constants):
    def recursiveFunc(index, arr):
            # iterate across all values in range between min and max with a step
        for constantValue in numpy.arange(constants[index]['min'], constants[index]['max']+1, constants[index]['step']):
            # convert to <int>
            arr.append(constantValue.item())

            # this is a last constant object in config
            if(index+1 >= constantsLength):
                result.append(arr.copy())
                arr.pop()
            # there is more constant objects in config
            else:
                recursiveFunc(index+1, arr)
                arr.pop()
    result = []
    constantsLength = len(constants)
    # 0 - start from first constant object
    recursiveFunc(0, [])
    log('constants variations length: ' + str(len(result)))
    return result