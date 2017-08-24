import pandas as pd
import numpy as np

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

#remove year from column label
weather2015['Date'] = weather2015['Date'].apply(lambda x: x[5:])
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

#plot 20xx max and mins

#calulate record breaking temps
