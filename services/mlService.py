import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np
from services.loggerService import log


from neupy import algorithms
from neupy.layers import *

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import explained_variance_score

import services.utilsService as utils

# TODO write doc
def getTrainNetworks(data):
    networks = []
    # generate network for each time interval
    for timeIntervalData in data:
        
        constantsSetArray = []
        concentrationVsTimeArray = []
        
        # arrange constants vs concentration lines in different arrays
        for constantsVsConcentration in timeIntervalData['data']:

            constantsSetArray.append(constantsVsConcentration['constantsSet'])
            concentrationVsTimeArray.append(
                constantsVsConcentration['concentrationLine'])
        
        # split-out validation dataset
        validation_size = 0.03
        seed = 7
        constantsSetArray_train, constantsSetArray_validation, concentrationVsTimeArray_train, concentrationVsTimeArray_validation = model_selection.train_test_split(
            constantsSetArray, concentrationVsTimeArray, test_size=validation_size, random_state=seed)
        
        concentrationVsTimeArray_train_2d = utils.get2dData(concentrationVsTimeArray_train)
        concentrationVsTimeArray_validation_2d = utils.get2dData(concentrationVsTimeArray_validation)

        max_depth = 50
        regr_multirf = RandomForestRegressor(n_estimators=100,
                                                          max_depth=max_depth,
                                                          random_state=0)
        regr_multirf.fit(concentrationVsTimeArray_train_2d, constantsSetArray_train)
        
        predictedForValidation = regr_multirf.predict(concentrationVsTimeArray_validation_2d)
        accuracyBreakBy = explained_variance_score(constantsSetArray_validation, predictedForValidation,  multioutput='raw_values')
        avarage = explained_variance_score(constantsSetArray_validation, predictedForValidation,  multioutput='uniform_average')
        
        log('random forest accuracy breakby:')
        log(accuracyBreakBy)
        log('random forest accuracy avarage:')
        log(avarage)
        networks.append(regr_multirf)

    return networks

def getPredictionsArray(networks,inputs):
    """
        Predicts based on input and network and returns an array of predicted values.
        Arguments should have the same array size
    """
    predictions = []
    for i in range(0,len(networks)):
        input_2d = [np.asarray(inputs[i]).ravel()]
        predictions.append(networks[i].predict(input_2d))

    log("predictions:" )
    log(predictions)
    return predictions
