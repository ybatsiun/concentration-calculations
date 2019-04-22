import numpy as np
from config import *


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def splitConcentrationsByTimeInterval(concentrations):
    return list(split(concentrations, CALCULATION_CONFIG["PARTS_TO_DIVIDE"]))


def get2dData(ThreeDimData):
    dataset_size = len(ThreeDimData)
    return np.asarray(ThreeDimData).reshape(dataset_size, -1)
