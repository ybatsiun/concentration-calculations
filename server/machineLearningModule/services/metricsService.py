from services.loggerService import log

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
            answersArray[a][i] = (
                abs(answersArray[a][i]-avarageValues[i])/avarageValues[i])*100


    log('relative error per answer in percent',True)
    log(answersArray,True)
