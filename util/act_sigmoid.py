import numpy as np


def sigmoid(z):
    return 1/(1 + np.exp(np.multiply(-1, z)))
