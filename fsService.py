import pickle

def writeToFile(content, fileName):
    file = open(fileName, "wb")
    pickle.dump(content, file)

    file.close()

    # with open (fileName, 'rb') as fp:
    #     itemlist = pickle.load(fp)

    # print(itemlist)
    
