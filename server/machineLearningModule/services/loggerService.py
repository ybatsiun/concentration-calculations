import services.fsService as fsService
import datetime
import time
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE_NAME = dir_path + '/../log.txt'


def log(line,printConsole = False):
    if(printConsole):
        print(line)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    formattedLine = "[{}]: {}\n".format(st, line)
    fsService.writeToTxtFile(formattedLine, FILE_NAME)
