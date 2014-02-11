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
            'Error on training data ===\n\nCorrectly Classified Instances {training_matches:^g} {training_accuracy:^g} %\nIncorrectly Classified Instances {training_misses:^g} {training_error:^g} %',
            'Error on test data ===\n\nCorrectly Classified Instances {testing_matches:^g} {testing_accuracy:^g} %\nIncorrectly Classified Instances {testing_misses:^g} {testing_error:^g} %',
        ]
        result = {}
        for pattern in pattern_list:
            match = parse.search(pattern, raw_output)
            if match is not None:
                result.update(match.named)
        return result

    def run_test(self, classifier, sample_size=None, options=''):
        logger.info('running test: [classifier=%s, size=%d/%d]',
                    classifier, sample_size, len(self.data.training_data))
        size = len(self.data.training_data) if sample_size is None else sample_size
        self.data.save_training_file(size)
        cmd = "java -cp /usr/share/java/weka.jar {} {} -t /tmp/train.arff -T /tmp/test.arff"
        logger.info(cmd.format(classifier, options))
        output = subprocess.check_output(cmd.format(classifier, options), shell=True)
        parsed_output = self.parse_tree_output(output)
        logger.info('results: %s', str(parsed_output))
        return {
            'sample_size': size,
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

    def run_multiple_sample_sizes(self, classifier, sample_sizes, options=''):
        self.results = []
        for size in sample_sizes:
            self.results.append(self.run_test(classifier, size, options=options))

    def run_multiple_classifiers(self, classifier_list, sample_size=None):
        self.results = []
        for classifier in classifier_list:
            self.results.append(self.run_test(classifier, sample_size))
