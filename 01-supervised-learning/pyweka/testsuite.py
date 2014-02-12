import subprocess
import logging
import parse
import pickle

import matplotlib.pyplot as plt

from classifiers import Classifiers
from dataset import DataSet


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class TestSuite(object):
    def __init__(self, data_file=None, results_file=None):
        self.classifiers = Classifiers()
        if data_file:
            self.data = DataSet(data_file)
            self.data.save_test_file()
        else:
            self.data = None
        if results_file:
            self.load_results(results_file)
        else:
            self.results = []

    @staticmethod
    def parse_tree_output(raw_output):
        pattern_list = [
            'Number of Leaves  : \t{leaf_count:^g}',
            'Size of the tree : \t{tree_size:^g}',
            'Time taken to build model: {run_time:^g} seconds',
        ]
        train_test_patterns = [
            'Correctly Classified Instances {matches:^g} {accuracy:^g} %\nIncorrectly Classified Instances {misses:^g} {error:^g} %',
            'Weighted Avg. {tp_rate:^g} {fp_rate:^g} {percision:^g} {recall:^g} {f_measure:^g} {roc_area:^g}',
        ]

        result = {}
        for pattern in pattern_list:
            match = parse.search(pattern, raw_output)
            if match is not None:
                result.update(match.named)
        for pattern in train_test_patterns:
            matches = [m for m in parse.findall(pattern, raw_output)]
            if len(matches) == 2:
                for k, v in matches[0].named.iteritems():
                    result['training_{}'.format(k)] = v
                for k, v in matches[1].named.iteritems():
                    result['testing_{}'.format(k)] = v
        return result

    def run_test(self, classifier, sample_size=None, options=''):
        logger.info('running test: [classifier=%s, size=%d/%d]',
                    classifier, sample_size, len(self.data.training_data))
        size = len(self.data.training_data) if sample_size is None else sample_size
        self.data.save_training_file(size)
        cmd = "java -cp /usr/share/java/weka.jar {} {} -i -t /tmp/train.arff -T /tmp/test.arff"
        logger.info(cmd.format(classifier, options))
        output = subprocess.check_output(cmd.format(classifier, options), shell=True)
        parsed_output = self.parse_tree_output(output)
        logger.info('results: %s', str(parsed_output))
        return {
            'sample_size': size,
            'options': options,
            'classifier': classifier,
            'raw_output': output,
            'results': parsed_output
        }

    def load_results(self, path):
        with open(path) as _file:
            self.results = pickle.load(_file)

    def save_results(self, path):
        with open(path, 'w') as _file:
            pickle.dump(self.results, _file)

    def plot_result(self, x_field, y_field, title='', show=False):
        fig, axes = plt.subplots()
        x = [r[x_field] for r in self.results]
        y = [r['results'][y_field] for r in self.results]
        axes.scatter(x, y)
        axes.set_xlabel(x_field)
        axes.set_ylabel(y_field)
        if title:
            axes.set_title(title)
        if show:
            fig.show()
        return fig, axes

    def run_multiple_tests(self, classifier, sample_size=None, options=None):
        self.results = []
        sample_size = len(self.data.training_data) if sample_size is None else sample_size
        options = '' if options is None else options
        sample_size_list = sample_size if isinstance(sample_size, list) else [sample_size]
        options_list = options if isinstance(options, list) else [options]
        try:
            for options in options_list:
                for size in sample_size_list:
                    self.results.append(self.run_test(classifier, size, options=options))
        except KeyboardInterrupt:
            print 'exiting'
            return

    def run_multiple_classifiers(self, classifier_list, sample_size=None):
        self.results = []
        for classifier in classifier_list:
            self.results.append(self.run_test(classifier, sample_size))
