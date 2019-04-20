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

from neupy import algorithms
from neupy.layers import *

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import explained_variance_score



def getTrainNetworks(data):

    # generate network for each time interval
    for timeIntervalData in data:
        constantsSetArray = []
        concentrationVsTimeArray = []
        # arrange constants vs concentratioLines in different arrays
        for constantsVsConcentration in timeIntervalData['data']:

            constantsSetArray.append(constantsVsConcentration['constantsSet'])
            concentrationVsTimeArray.append(
                constantsVsConcentration['concentrationLine'])
        
        # Split-out validation dataset
        validation_size = 0.03
        seed = 7
        constantsSetArray_train, constantsSetArray_validation, concentrationVsTimeArray_train, concentrationVsTimeArray_validation = model_selection.train_test_split(
            constantsSetArray, concentrationVsTimeArray, test_size=validation_size, random_state=seed)
        dataset_size = len(concentrationVsTimeArray_train)
        concentrationVsTimeArray_train_2d = np.asarray(concentrationVsTimeArray_train).reshape(dataset_size,-1)
        

        dataset_size = len(concentrationVsTimeArray_validation)
        concentrationVsTimeArray_validation_2d = np.asarray(concentrationVsTimeArray_validation).reshape(dataset_size,-1)

        max_depth = 50
        regr_multirf = RandomForestRegressor(n_estimators=100,
                                                          max_depth=max_depth,
                                                          random_state=0)
        regr_multirf.fit(concentrationVsTimeArray_train_2d, constantsSetArray_train)
        
        predictedForValidation = regr_multirf.predict(concentrationVsTimeArray_validation_2d)
        accuracyBreakBy = explained_variance_score(constantsSetArray_validation, predictedForValidation,  multioutput='raw_values')
        avarage = explained_variance_score(constantsSetArray_validation, predictedForValidation,  multioutput='uniform_average')
        
        print('random forest accuracy breakby:')
        print(accuracyBreakBy)
        print('random forest accuracy avarage:')
        print(avarage)

    return 'mock'