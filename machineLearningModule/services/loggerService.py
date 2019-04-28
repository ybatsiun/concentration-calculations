import services.fsService as fsService
import datetime
import time

FILE_NAME = 'machineLearningModule/log.txt'

def log(line):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    formattedLine = "[{}]: {}\n".format(st,line)
    fsService.writeToTxtFile(formattedLine,FILE_NAME)