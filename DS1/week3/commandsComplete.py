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

#number of rows that were lost
len(df1) - len(df) 

# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.

avgGDP = df[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1).sort_values(ascending=False)

#By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
avgGDPCountry = df[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1).sort_values(ascending=False).index[5]
df.get_value(avgGDPCountry,'2015') - df.get_value(avgGDPCountry,'2006')

#What is the mean Energy Supply per Capita?
meanESpC = df[['Energy Supply per Capita']].mean(axis=0).values[0]

#What country has the maximum % Renewable and what is the percentage?
list(zip(df[['% Renewable']].idxmax(axis=0),df[['% Renewable']].max(axis=0)))

# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
df['Citations Ratio'] = df['Self-citations']/df['Citations']
list(zip(df[['Citations Ratio']].idxmax(axis=0),df[['Citations Ratio']].max(axis=0)))

# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
df['Population Estimate'] = df['Energy Supply']/df['Energy Supply per Capita']
thirdCountryPop = df[['Population Estimate']].max(axis=1).sort_values(ascending=False).index[2]

# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? 
# Use the .corr() method, (Pearson's correlation).
df['Citable docs per Capita'] = df['Citable documents'] / df['Population Estimate']
df['Citable docs per Capita'].corr(df['Energy Supply per Capita'])

# Create a new column with a 1 if the country's % Renewable value is at or above the median 
# for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# This function should return a series named HighRenew whose index is 
# the country name sorted in ascending order of rank.
df.sort_values(['Rank'],ascending=True, inplace=True)
medianRenew = df[['% Renewable']].median(axis=0).values[0]
df['Median Renew'] = np.where(df['% Renewable'] >= medianRenew, 1, 0)

# Use the following dictionary to group the Countries by Continent, 
# then create a dateframe that displays the sample size (the number of countries in each 
# continent bin), and the sum, mean, and std deviation for the estimated population 
# of each country.
#This function should return a DataFrame with index named Continent 
# ['Asia', 'Australia', 'Europe', 'North America', 'South America'] 
# and columns ['size', 'sum', 'mean', 'std']

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
df['Continent'] = pd.Series(ContinentDict)
df['Population Estimate'] = df['Energy Supply']/df['Energy Supply per Capita']
qq = df.groupby('Continent')['Population Estimate'].agg({'size':np.size,'min':min,'median':np.median,'max':max})

# Cut % Renewable into 5 bins. Group Top15 by the Continent, 
# as well as these new % Renewable bins. How many countries are in each of these groups?
# This function should return a Series with a MultiIndex of Continent, 
# then the bins for % Renewable. Do not include groups with no countries.

df['Renewable Bins'] = pd.cut(df['% Renewable'],5)
qq = df.groupby(['Continent','Renewable Bins'])['Continent'].agg(len)

# Convert the Population Estimate series to a string with thousands separator 
# (using commas). Do not round the results
df['Population Estimate'] = df['Population Estimate'].apply(lambda x: "{:,}".format(x))