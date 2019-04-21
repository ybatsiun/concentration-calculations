import pickle
import json


def writeBinaryToFile(content, fileName):
    file = open(fileName, "wb")
    pickle.dump(content, file)
    file.close()


def writeJsonToFile(content, fileName):
    file = open(fileName, "w")
    json.dump(content, file)
    file.close()

def readJsonFile(fileName):
    with open(fileName, 'r') as f:
        datastore = json.load(f)
    return datastore