import numpy as np


def mean(x):
    total = np.sum(x, axis=0)
    count = x.shape[0]
    return total / count


def variance(x):
    deviations = x - mean(x)
    squared = deviations**2
    return np.sum(squared, axis=0) / x.shape[0]


def std(x):
    return np.sqrt(variance(x))


def median(x):
    s = np.sort(x, axis=0)
    n = x.shape[0]
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2 - 1] + s[n // 2]) / 2


def zscore(x):
    centered = x - mean(x)
    return centered / std(x)
