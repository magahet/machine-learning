#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.tools.plotting import parallel_coordinates


data = read_csv(sys.argv[1])
parallel_coordinates(data[:1000], 'class')
#plt.xticks(rotation=45)
plt.show()
