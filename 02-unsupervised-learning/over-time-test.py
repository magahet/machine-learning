#!/usr/bin/env python

#import os
#import sys
import subprocess
import matplotlib.pyplot as plt

# get number of iterations required to find max value
# for each combination of bit lengths, eval functions, and algorithms

# params: bit_length, ef, oa, iterations
cmd_tmpl = 'java -cp ABAGAIL.jar opt.test.MultiTest {} {} {} {}'
test_runs = 10
bit_length = 80
max_iterations = 10000

ef_titles = ['entropy', 'count_ones', 'four_peaks', 'flip-flop']
oa_titles = ['RHC', 'SA', 'GA', 'MIMIC']

for ef in range(1, 4):
    f, ax = plt.subplots(4, sharex=True)
    for oa in range(4):
        print 'Running: {}, {}'.format(ef_titles[ef], oa_titles[oa])
        cmd = cmd_tmpl.format(bit_length, ef, oa, max_iterations)
        for i in range(test_runs):
            lines = subprocess.check_output(cmd, shell=True).splitlines()
            x = []
            y = []
            for l in lines:
                parts = l.split(',')
                x.append(int(parts[0]))
                y.append(float(parts[1]))
            ax[oa].plot(x, y)
        ax[oa].set_title(oa_titles[oa])
    f.text(0.5, 0.95, ef_titles[ef], ha='center', va='center')
    f.text(0.5, 0.04, 'evaluations', ha='center', va='center')
    f.text(0.06, 0.5, 'fitness score', ha='center', va='center', rotation='vertical')
    f.show()
