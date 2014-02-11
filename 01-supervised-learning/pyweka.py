#!/usr/bin/env python

import argparse
import logging
import pyweka
import os
import glob


def run_multiple_samples_and_classifiers(_dir='.'):
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    if not os.path.exists('{}/learning-curve-10to2000'.format(_dir)):
        os.makedirs('{}/learning-curve-10to2000'.format(_dir))

    sizes = range(10, 2001, 10)

    profiles = {
        'c4.5': (c.j48, sizes, ''),
        'boosting-stump': (c.boost_stump, sizes,  ''),
        'perceptron': (c.perceptron, sizes,  ''),
        'svm-polykernel': (c.svm, sizes,  ''),
        'k-nn-1': (c.ibk, sizes,  '-K 1'),
        'k-nn-3': (c.ibk, sizes,  '-K 3'),
        'k-nn-5': (c.ibk, sizes,  '-K 5')
    }

    for name, p in profiles.iteritems():
        if os.path.exists('{}/learning-curve-10to2000/{}.pkl'.format(_dir, name)):
            t.load_results('{}/learning-curve-10to2000/{}.pkl'.format(_dir, name))
        else:
            t.run_multiple_sample_sizes(*p)
            t.save_results('{}/learning-curve-10to2000/{}.pkl'.format(_dir, name))
        f, a = t.plot_result('sample_size', 'training_error', '{} training error by training size'.format(name))
        f.savefig('{}/learning-curve-10to2000/train-error-{}.pdf'.format(_dir, name))
        f, a = t.plot_result('sample_size', 'testing_error', '{} testing error by training size'.format(name))
        f.savefig('{}/learning-curve-10to2000/test-error-{}.pdf'.format(_dir, name))
        f, a = t.plot_result('sample_size', 'run_time', '{} training time by training size'.format(name))
        f.savefig('{}/learning-curve-10to2000/runtime-{}.pdf'.format(_dir, name))


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
