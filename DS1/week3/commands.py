import pandas as pd
import numpy as np

energy = pd.read_csv('EnergyIndicators.csv', index_col=0)
energy = energy.replace('...',np.NaN)
energy.drop('Unnamed: 4', axis=1, inplace=True)
energy = energy.apply(pd.to_numeric, errors='ignore')
energy.loc[:,'Energy Supply'] *= 1000000  #convert from petajoules to joules
list(energy) #list the columns
list(energy.index.values) #list the indexes


GDP = pd.read_csv('world_bank.csv', index_col=0)

ScimEn = pd.read_csv('scimagojr-3.csv', index_col=0)

df_merged = energy.merge(GDP,how='inner',left_index=True, right_index = True) #merge on two indexes
df1_merged = pd.merge(df_merged,ScimEn,how='inner',left_index=True,right_on='Country') #merge on a column and an index



