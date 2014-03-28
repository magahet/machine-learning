from sklearn.decomposition import FastICA
import pandas
import sys
import scipy
import numpy


def run_ica(data, n):
    ica = FastICA(n)
    return ica.fit_transform(data.as_matrix())


def get_best_n(data):
    print 'finding best k'
    max_k = -1
    max_n = -1
    for n in range(1, data.shape[1]):
        result = run_ica(data, n)
        k = max(numpy.absolute(scipy.stats.kurtosis(result)))
        print n, k
        max_k = k if k > max_k else max_k
        max_n = n if k > max_k else max_n
    return max_n


data = pandas.read_csv(sys.argv[1])
