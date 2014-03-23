#!/usr/bin/env python

import os
#import sys
#import subprocess
import matplotlib.pyplot as plt

# get number of iterations required to find max value
# for each combination of bit lengths, eval functions, and algorithms

# params: bit_length, ef, oa, iterations
cmd_tmpl = 'java -cp ABAGAIL.jar opt.test.MultiTest {} {} {} {}'
test_runs = 10

ef_titles = ['entropy', 'count_ones', 'four_peaks', 'flip-flop']
oa_titles = ['RHC', 'SA', 'GA', 'MIMIC']

for ef in range(4):
    f, ax = plt.subplots()
    for oa in range(4):
        print 'Running: {}, {}'.format(ef_titles[ef], oa_titles[oa])
        bit_range = range(10, 90, 10)
        vals = []
        path = 'part1.2/eval-data/{}-{}'.format(ef, oa)
        if os.path.exists(path):
            vals = [float(l.strip()) for l in open(path).readlines()]
        else:
            continue
        #needs_save = True if len(vals) < len(bit_range) else False
        #for bit_length in bit_range[len(vals):]:
            #cmd = cmd_tmpl.format(bit_length, ef, oa, 0)
            #num = int(subprocess.check_output(cmd, shell=True))
            #sys.stdout.write('{}, '.format(num))
            #sys.stdout.flush()
            #vals.append(num)
        #print
        #if needs_save:
            #with open(path, 'w') as file_:
                #file_.write('\n'.join([str(i) for i in vals]))
        ax.plot(range(10, (10 * len(vals)) + 10, 10), vals, label=oa_titles[oa])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=2)
    ax.set_yscale('log')
    ax.set_title(ef_titles[ef])
    ax.set_xlabel('input length')
    ax.set_ylabel('evaluations')
    f.show()
