from sklearn.decomposition import FastICA
import pandas
import sys
import scipy
import numpy
from tabulate import tabulate


def run_ica(data, n):
    ica = FastICA(n)
    return ica.fit_transform(data.as_matrix())


def get_best_n(data):
    print 'finding best k'
    results = []
    for n in range(1, data.shape[1]):
        result = run_ica(data, n)
        normalized_results = numpy.absolute(scipy.stats.kurtosis(result))
        results.append([str(i) for i in scipy.stats.describe(normalized_results)])
    print tabulate(results, headers=['n', 'max/min', 'mean', 'var', 'skew', 'kurtosis'])


data = pandas.read_csv(sys.argv[1])
