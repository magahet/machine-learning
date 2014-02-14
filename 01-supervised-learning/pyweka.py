#!/usr/bin/env python

import argparse
import logging
import pyweka
import os
import glob


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def run_multiple_samples_and_classifiers(names, _dir='.'):
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    if not os.path.exists('{}'.format(_dir)):
        os.makedirs('{}'.format(_dir))

    group_dir = '{}/k-nn'.format(_dir)
    if not os.path.exists(group_dir):
        os.makedirs(group_dir)
    experiments = {
        'c4.5': (c.j48, range(10, 2001, 10), ''),
        'boosting-stump': (c.boost_stump, range(10, 2001, 10),  ''),
        'perceptron': (c.perceptron, range(10, 2001, 10),  ''),
        'svm-polykernel': (c.svm, range(10, 2001, 10),  ''),
        'k-nn-1': (c.ibk, range(10, 2001, 10),  '-K 1'),

        'learning-rate': (c.perceptron, 1000,  ['-L {}'.format(n) for n in drange(0.1, 1, 0.1)]),
        'momentum': (c.perceptron, 1000,  ['-M {}'.format(n) for n in drange(0.1, 1, 0.1)]),
        'iterations': (c.perceptron, 1000,  ['-N {}'.format(n) for n in range(10, 1001, 10)]),

        'boosting-stump': (c.boost_stump, [1000],  ['-I {}'.format(n) for n in range(1, 1001, 1)]),

        'svm-polykernel': (c.svm, [1000],  ['-K "weka.classifiers.functions.supportVector.PolyKernel -E {}"'.format(n) for n in range(1, 11)]),
        'svm-rbf': (c.svm, [1000],  ['-K "weka.classifiers.functions.supportVector.RBFKernel -G {}"'.format(n) for n in drange(0.001, 0.4, 0.001)]),

        'k-nn': (c.ibk, 1000,  ['-K {}'.format(n) for n in range(1, 101)]),
    }

    results = {}
    for name, p in experiments.iteritems():
        if name not in names:
            continue
        if os.path.exists('{}/{}.pkl'.format(group_dir, name)):
            t.load_results('{}/{}.pkl'.format(group_dir, name))
        else:
            t.run_multiple_tests(*p)
            t.save_results('{}/{}.pkl'.format(group_dir, name))
        results[name] = t.results
    return results
    #f, a = t.plot_result('sample_size', 'training_error', '{} training error by training size'.format(name))
        #f.savefig('{}/train-error-{}.pdf'.format(group_dir, name))
        #f, a = t.plot_result('sample_size', 'testing_error', '{} testing error by training size'.format(name))
        #f.savefig('{}/test-error-{}.pdf'.format(group_dir, name))
        #f, a = t.plot_result('sample_size', 'run_time', '{} training time by training size'.format(name))
        #f.savefig('{}/runtime-{}.pdf'.format(group_dir, name))
    #pyweka.plot_multiple(results_list, 'sample_size', 'testing_f_measure', 'training_f_measure', 'classifier', 'training set size', 'weighted f-score', True)


def load_multiple_results(pattern):
    results_list = []
    for path in glob.glob(pattern):
        t = pyweka.TestSuite(results_file=path)
        results_list.append(t.results)
    return results_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='weka wrapper')
    parser.add_argument('--datafile', '-d', help='file to sample')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    c = pyweka.Classifiers()
    t = pyweka.TestSuite(args.datafile)
