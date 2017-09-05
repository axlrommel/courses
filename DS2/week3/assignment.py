import pandas as pd
import numpy as np
import math
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

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
threshold = 38000
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xlocations = np.array(range(len(data)))+width
barlist = ax.bar(xlocations, data, yerr=error, width=width, error_kw=dict(lw=1, capsize=10, capthick=1))
barlist[0].set_color('r')
ax.set_xticks(xlocations)
ax.set_xticklabels(labels)
ax.set_xlim(0, xlocations[-1]+width*2)
plt.title("Average Ratings on the Training Set")
ax.plot([0., 4.5], [threshold, threshold], "k--")
plt.gca().get_xaxis().tick_bottom()
plt.gca().get_yaxis().tick_left()
plt.show()
