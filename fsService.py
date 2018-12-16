import pickle

def writeToFile(content, fileName):
    file = open(fileName, "wb")
    pickle.dump(content, file)

    file.close()