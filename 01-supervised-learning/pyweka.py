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


def run_multiple_samples_and_classifiers(_dir='.'):
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    if not os.path.exists('{}'.format(_dir)):
        os.makedirs('{}'.format(_dir))

    sizes = range(10, 2001, 10)

    group_dir = '{}/learning-curve-10to2000'.format(_dir)
    if not os.path.exists(group_dir):
        os.makedirs(group_dir)
    profiles = {
        'c4.5': (c.j48, sizes, ''),
        'boosting-stump': (c.boost_stump, sizes,  ''),
        'perceptron': (c.perceptron, sizes,  ''),
        'svm-polykernel': (c.svm, sizes,  ''),
        'k-nn-1': (c.ibk, sizes,  '-K 1'),
        #'k-nn-3': (c.ibk, sizes,  '-K 3'),
        #'k-nn-5': (c.ibk, sizes,  '-K 5'),

        #'learning-rate': (c.perceptron, 1000,  ['-L {}'.format(n) for n in drange(0.1, 10, 0.1)]),
        #'momentum': (c.perceptron, 1000,  ['-M {}'.format(n) for n in drange(0.1, 10, 0.1)]),
        #'iterations': (c.perceptron, 1000,  ['-N {}'.format(n) for n in range(10, 2001, 10)]),
    }

    results_list = []
    for name, p in profiles.iteritems():
        print name
        if os.path.exists('{}/{}.pkl'.format(group_dir, name)):
            t.load_results('{}/{}.pkl'.format(group_dir, name))
        else:
            t.run_multiple_tests(*p)
            t.save_results('{}/{}.pkl'.format(group_dir, name))
        results_list.append(t.results)
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
