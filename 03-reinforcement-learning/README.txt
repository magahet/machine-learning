Overview
========

All experiments were conducted using Weka 3.6.6. A number of automated experiments were performed with a python script and module included here (pyweka). This code acts as a utility wrapper around the Weka CLI and provides abstraction objects and functions for performing the following:

    - handling arff data
    - calling the weka cli app with various parameters
    - parsing the experiment output
    - caching results in native data formats
    - plotting results with matplotlib
    
Interaction with the utility script and module was done in Ipython.

The python code is intended only to assist in performing the various experiments. It is by no means robust. The core machine learning tasks are all performed in Weka, and many of the experiments described in my analysis were performed within the Weka GUI.



Requirements
============

    Weka 3.6.6
    Python 2.7
    Ipython or Python interactive console



Tutorial
=====

## Run a single experiment

# start ipython (or python console) and run pyweka.py in interactive mode
$ ipython -i pyweka.py

# instantiate the TestSuite class with the path to the full dataset arff
>>> t = pyweka.TestSuite('data/adult/adult.data.arff')

# run the predefined experiment and use 'data/adult' directory to cache results
# experiments are defined in pyweka.py
>>> rs = run_multiple_samples_and_classifiers(['k-nn'], 'data/adult/')

# create a chart to display the results of the experiment
>>> fig, axis = pyweka.plot_result(rs['k-nn'], y_field='testing_error', y2_field='training_error', x=[x for x in range(1, 11)], title='k-nn error by k', x_label='k', show=True)

# save the resulting chart
>>> fig.savefig('data/adult/k-nn/error.pdf')



## Run performance experiments on a set of learners

# start ipython (or python console) and run pyweka.py in interactive mode
$ ipython -i pyweka.py

# instantiate the TestSuite class with the path to the full dataset arff
>>> t = pyweka.TestSuite('data/adult/adult.data.arff')

# define the set of experiments to perform
# these are defined in pyweka.py
>>> stacked_experiments = ['c4.5', 'boosting-stump', 'perceptron', 'svm-polykernel', 'k-nn-1']

# run the experiments and use 'data/adult' directory to cache results
>>> rs = run_multiple_samples_and_classifiers(stacked_experiments, 'data/adult/')

# create a stacked set of charts for the various result sets
>>> fig, axises = pyweka.plot_multiple(rs.values(), 'sample_size', 'testing_f_measure', 'training_f_measure', title_field='classifier', x_label='training set size', y_label='weighted f-score', show=True)

# save the resulting chart
>>> fig.savefig('data/adult/learning-curve-10to2000/stacked-fscore.pdf')

