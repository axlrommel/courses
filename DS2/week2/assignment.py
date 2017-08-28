import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.finance import date2num
import datetime as datetime

fname = "fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv"
weather = pd.read_csv(fname)

#remove station
weather = weather[['Date','Element','Data_Value']]

# add decimal to temperature
weather['Data_Value'] = weather['Data_Value'].apply(lambda x: x/10)

#remove feb 29
weather = weather.loc[~weather['Date'].str.endswith('02-29')]

#separate by years
weather2015 = weather.loc[weather['Date'].str.startswith('2015')]
weather20xx = weather.loc[~weather['Date'].str.startswith('2015')]

#remove year from column label for 2000-2014
weather20xx['Date'] = weather20xx['Date'].apply(lambda x: x[5:])

#get max and mins
weather2015max = weather2015.loc[weather2015['Element'] == 'TMAX']
weather2015min = weather2015.loc[weather2015['Element'] == 'TMIN']
weather2015max = weather2015max.groupby('Date')['Data_Value'].agg({'max':max})
weather2015min = weather2015min.groupby('Date')['Data_Value'].agg({'min':min})

#get max and mins
weather20xxmax = weather20xx.loc[weather20xx['Element'] == 'TMAX']
weather20xxmin = weather20xx.loc[weather20xx['Element'] == 'TMIN']
weather20xxmax = weather20xxmax.groupby('Date')['Data_Value'].agg({'max':max})
weather20xxmin = weather20xxmin.groupby('Date')['Data_Value'].agg({'min':min})

# let's reindex the dfs
weather2015max.reset_index(inplace = True)
weather2015min.reset_index(inplace = True)
weather20xxmax.reset_index(inplace = True)
weather20xxmin.reset_index(inplace = True)

#plot 20xx max and mins
fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(weather20xxmax.index, weather20xxmax['max'])
plt.plot(weather20xxmin.index, weather20xxmin['min'])

#color in between the two graphs
l1,l2 = plt.gca().get_lines()
x,y =l1.get_data()
x1,y1 =l2.get_data()
plt.gca().fill_between(x,y,y1,alpha=.1)

#first days of each month [  1,  32,  60,  91, 121, 152, 182, 213, 244, 274, 305, 335]
xticks = (pd.date_range('1/1/2015','31/12/2015', freq = 'M') - 1 + pd.Timedelta('1D')).strftime('%-j').astype(int)

#months ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
xticks_labels = pd.to_datetime(xticks, format='%j').strftime('%b')

ax.set_xlim(1,365)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks_labels)
fig.autofmt_xdate(ha='left', rotation = None)

#calulate record breaking temps and plot them
ax.plot([5,345],[20,25],'o')
plt.show()


