import os
import random
import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class DataSet(object):
    def __init__(self, path, training_ratio=0.66):
        self.load_from_file(path)
        self.split_test_data(training_ratio)

    def clean_dir(self):
        for filename in os.listdir('/tmp'):
            if filename.endswith('.arff'):
                os.remove(os.join('/tmp', filename))

    def save_test_file(self):
        self.write_file('/tmp/test.arff', self.testing_data)

    def save_training_file(self, sample_size=None):
        sample_size = len(self.training_data) if sample_size is None else sample_size
        self.write_file('/tmp/train.arff',
                        random.sample(self.training_data, sample_size))

    def write_file(self, path, data):
        with open(path, 'w') as _file:
            _file.write(self.header)
            _file.write('\n')
            _file.write('\n'.join(data))

    def load_from_file(self, path):
        with open(path) as _file:
            header_list = []
            while True:
                line = _file.readline()
                if line:
                    header_list.append(line.rstrip())
                    if line.startswith('@data'):
                        break
                else:
                    raise Exception('Error reading arff file')
            self.header = '\n'.join(header_list)
            self.full_data = [l.rstrip() for l in _file.readlines()]

    def split_test_data(self, training_ratio):
        split_index = int(len(self.full_data) * training_ratio)
        self.training_data = self.full_data[:split_index]
        self.testing_data = self.full_data[split_index:]
