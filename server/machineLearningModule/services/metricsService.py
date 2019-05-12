from services.loggerService import log
import numpy as np


def getRelativeError(answersArray):
    avarageValues = []
    # make 2d array
    for i in range(0, len(answersArray)):
        answersArray[i] = answersArray[i].reshape(-1)

    for i in range(0, len(answersArray[0])):
        sum = 0
        for answerSet in answersArray:
            sum += answerSet[i]
        avarageValues.append(sum/len(answersArray))

    for a in range(0, len(answersArray)):
        for i in range(0, len(answersArray[a])):
            value = (abs(answersArray[a][i]-avarageValues[i])/avarageValues[i])*100
            answersArray[a][i] = round(value,3)


    log('relative error per answer in percent',True)
    log(np.array(answersArray).tolist(),True)
