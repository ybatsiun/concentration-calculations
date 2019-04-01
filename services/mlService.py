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
        validation_size = 0.20
        seed = 7
        constantsSetArray_train, constantsSetArray_validation, concentrationVsTimeArray_train, concentrationVsTimeArray_validation = model_selection.train_test_split(
            constantsSetArray, concentrationVsTimeArray, test_size=validation_size, random_state=seed)

        dataset_size = len(concentrationVsTimeArray_train)
        concentrationVsTimeArray_train_2d = np.asarray(concentrationVsTimeArray_train).reshape(dataset_size,-1)
        

        dataset_size = len(concentrationVsTimeArray_validation)
        concentrationVsTimeArray_validation_2d = np.asarray(concentrationVsTimeArray_validation).reshape(dataset_size,-1)

        # Make predictions on validation dataset
        knn = SVC(gamma=0.00001, C=100)
        knn.fit(concentrationVsTimeArray_train_2d, constantsSetArray_train)
        predictions = knn.predict(concentrationVsTimeArray_validation_2d)
        print(accuracy_score(constantsSetArray_validation, predictions))
        print(confusion_matrix(constantsSetArray_validation, predictions))
        print(classification_report(constantsSetArray_validation, predictions))
            
    return 'mock'