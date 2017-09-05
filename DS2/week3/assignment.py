import pandas as pd
import numpy as np
import math
from matplotlib.pyplot import *

# by using the random.seed(), we get repeatable results
np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

# transpose the data
df1 = df.T

df2 = df1.describe()

#calculate 95% confidence interval for the mean
df3 = df2.T
df3['95_conf'] = df3['std'].apply(lambda x: 1.96*x/math.sqrt(3650))
labels = df3.index
data = df3['mean']
error = df3['95_conf']

width = 0.5
xlocations = np.array(range(len(data)))+width
bar(xlocations, data, yerr=error, width=width, error_kw=dict(lw=1, capsize=10, capthick=1))
xticks(xlocations, labels)
xlim(0, xlocations[-1]+width*2)
title("Average Ratings on the Training Set")
gca().get_xaxis().tick_bottom()
gca().get_yaxis().tick_left()

show()
