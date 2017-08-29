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
weather2015max = weather2015max.groupby('Date')['Data_Value'].agg({'max2015':max})
weather2015min = weather2015min.groupby('Date')['Data_Value'].agg({'min2015':min})

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

weather20xxmax['maxF'] = weather20xxmax['max'].apply(lambda x: x*9/5 + 32)
weather20xxmin['minF'] = weather20xxmin['min'].apply(lambda x: x*9/5 + 32)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 10,
        }

#plot 20xx max and mins
fig = plt.figure()
plt.title(
    'Max and Min Temperatures in Ann Arbor, MI between 2005 and 2014,\nand 2015 record breaking temperatures',
    fontdict=font)
ax = fig.add_subplot(111)

l1 = ax.plot(weather20xxmax.index, weather20xxmax['max'],label = 'Max Temperatures')
l2 = ax.plot(weather20xxmin.index, weather20xxmin['min'],label = 'Min Temperatures')

#color in between the two graphs
l1,l2 = plt.gca().get_lines()
x,y =l1.get_data()
x1,y1 =l2.get_data()
plt.gca().fill_between(x,y,y1,alpha=.1)

#first days of each month [  1,  32,  60,  91, 121, 152, 182, 213, 244, 274, 305, 335]
xticks = (pd.date_range('1/1/2015','31/12/2015', freq = 'M') -1 + pd.Timedelta('1D')).strftime('%-j').astype(int)

#months ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
xticks_labels = pd.to_datetime(xticks, format='%j').strftime('%b')

ax.set_xlim(1,365)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks_labels)
ax.set_yticks([-30,0,40])
ax.set_ylim(-40,43.3)
ax.set_yticklabels(['-30 °C','0 °C','40 °C'])
ax2 = ax.twinx()
ax2.set_yticks([-22,32,95])
ax2.set_yticklabels(['-22 °F','32 °F','95 °F'])
ax2.set_ylim(-40,110)
fig.autofmt_xdate(ha='left', rotation = None)

#calulate record breaking temps and plot them
max_ar_idx = []
max_ar_val = []
df_max = pd.merge(weather20xxmax,weather2015max,how='inner',left_index=True, right_index = True)
for index, row in df_max.iterrows():
    if row['max2015'] > row['max'] :
        max_ar_idx.append(index)
        max_ar_val.append(row['max2015'])

min_ar_idx = []
min_ar_val = []
df_min = pd.merge(weather20xxmin,weather2015min,how='inner',left_index=True, right_index = True)
for index, row in df_min.iterrows():
    if row['min2015'] < row['min'] :
        min_ar_idx.append(index)
        min_ar_val.append(row['min2015'])

l3, = ax.plot(max_ar_idx,max_ar_val, 'o') #the comma after l3 is important!
l4, = ax.plot(min_ar_idx,min_ar_val, 'x')

lines = [l1,l2,l3,l4]

plt.legend(lines,('2005 - 2014 High Temps','2005 - 2014 Low Temps',
    '2015 Record Highs','2015 Record Lows'), loc=8) #loc = 8 center low
plt.show()


