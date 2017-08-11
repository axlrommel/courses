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
df1_merged['Rank'] = df1_merged.index
df1 = df1_merged.set_index(['Country'])
columns_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
df = df1[columns_to_keep]
df = df.loc[df['Rank'] < 16]

#df.to_csv('combined1.csv')
