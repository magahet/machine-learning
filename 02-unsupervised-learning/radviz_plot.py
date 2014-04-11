#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.tools.plotting import radviz


data = read_csv(sys.argv[1])
radviz(data[:1000], 'cluster')
#plt.xticks(rotation=45)
plt.show()
