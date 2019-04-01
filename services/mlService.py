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

def getTrainNetworks(data):

    # Spot Check Algorithms
    # models = []
    # models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    # models.append(('LDA', LinearDiscriminantAnalysis()))
    # models.append(('KNN', KNeighborsClassifier()))
    # models.append(('CART', DecisionTreeClassifier()))
    # models.append(('NB', GaussianNB()))
    # models.append(('SVM', SVC(gamma='auto')))

    constantsSetArray = []
    concentrationsArray = []
    for constantsSet,concentrations in data:
        constantsSetArray.append(constantsSet)
        concentrationsArray.append(concentrations)
    return 'mock'