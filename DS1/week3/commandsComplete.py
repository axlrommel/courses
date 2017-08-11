import pandas as pd
import numpy as np

energy = pd.read_excel('Energy Indicators.xls', skiprows = [17], parse_cols = "C:F", header = 16, skip_footer=38, 
names = ['Energy Supply', 'Energy Supply per Capita', '% Renewable'])
energy.index.name = 'Country'
energy = energy.replace('...',np.NaN)
energy.loc[:,'Energy Supply'] *= 1000000
energy['Country1'] = energy.index
energy['Country1'].replace('[0-9]','',inplace=True, regex=True)
energy['Country1'].replace(' \(.+','',inplace=True,regex=True)
dicts = {"Republic of Korea": "South Korea",
             "United States of America": "United States",
             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
             "China, Hong Kong Special Administrative Region": "Hong Kong"}
energy['Country1'].replace(dicts,inplace=True)
energy.set_index('Country1', inplace = True)
energy.index.names = ['Country']

GDP = pd.read_csv('world_bank.csv', index_col=0, header = 4)
GDP['Country1'] = GDP.index
dicts1 = {"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"}
GDP['Country1'].replace(dicts1,inplace=True)
# make sure it worked : GDP.loc[GDP['Country1'] == 'Iran']
GDP.set_index('Country1', inplace = True)
GDP.index.names = ['Country Name']

ScimEn = pd.read_excel('scimagojr-3.xlsx')

df_merged = energy.merge(GDP,how='inner',left_index=True, right_index = True) #merge on two indexes
df1_merged = pd.merge(df_merged,ScimEn,how='inner',left_index=True,right_on='Country') #merge on a column and an index
df1_merged['Rank'] = df1_merged.index
df1 = df1_merged.set_index(['Country'])
columns_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
df = df1[columns_to_keep]
df = df.loc[df['Rank'] < 16]
df.loc[:,'Rank'] += 1