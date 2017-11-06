# Overview
#Tornadoes can be very deadly and destructive. In order to understand how 
# strong tornadoes can get, scientists commonly use the Fujita scale, 
# which rates tornadoes by damage caused. On one side of the Fujita scale 
# are tornadoes of category EF0, which may damage trees but will not cause 
# substantial damage to homes and buildings. On the other side of the scale, 
# tornadoes of category EF5 are the strongest type of tornadoes, they are 
# very damaging to structures and are often the most deadly. 
# Most of the EF5 tornadoes occur in the Midwest and Southern United States. 
# In this exercise we want to look at where exactly the strongest tornadoes 
# occur, what months they are more likely to occur and how many deaths 
# they are responsible for.

#The source for the data is the wikipedia page on the list of F5 and EF5 
# tornadoes from 1950 until 2015

import pandas as pd

df1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_F5_and_EF5_tornadoes')

#read 3rd and 4th table, drop first row and last column on each
dfa = df1[2].drop(df1[2].index[0]).drop([4], axis=1)
dfb = df1[3].drop(df1[3].index[0]).drop([4], axis=1)

#concatenate 3rd table (1950-1999) and 4th table (2000 - present)
df = pd.concat([dfa,dfb])

#look at the first 10 records
df.head(10)

#look at the last 5 records
df.tail()

#number of rows
len(df)

#list the column names
df.columns

#rename columns
df.columns = ['Month-Day'  ,'Year'  ,'Location','Deaths']

#cleanup the data
df['Year']=df['Year'].apply(lambda x: str(x)[-4:])
df['Month-Day'] = df['Month-Day'].apply(lambda x: str(x)[-len(x)+x.index("!")+1:])
df['Deaths'] = df['Deaths'].apply(lambda x: str(x)[-len(x)+x.index("♠")+1:]).apply(pd.to_numeric)

# extract the month from the 'Month-Day' column and put it in column called 'Month'
#drop the 'Month-Day' column
df['Month'] = df['Month-Day'].apply(lambda x: str(x)[:-len(x)+x.index(" ")+1]).apply(lambda x: x.strip())
df = df.drop('Month-Day', 1)

#create a separate column where you just list the state/country, use the last comma in 
# the Location field to separate it. Drop the Location column
df['Loc'] = df['Location'].apply(lambda x: str(x)[-len(x)+x.rfind(",")+1:]).apply(lambda x: x.strip())
df = df.drop('Location',1)

# using 'isin' create two dataframes, one with the data that have a loc in one of the
# states in the following list, the other without

states = ['Wisconsin', 'Texas', 'Oklahoma', 'Minnesota', 'Alabama', 'Tennessee', 'Kansas', 
'Pennsylvania', 'South Dakota', 'Iowa', 'Ohio', 'Kentucky', 'Indiana', 'Nebraska', 'Illinois', 
'North Dakota', 'Missouri', 'Michigan', 'Mississippi', 'Massachusetts','Louisiana','Arkansas']
df_us = df.loc[df['Loc'].isin(states)]
df_non_us = df.loc[~df['Loc'].isin(states)]

#stats on the numeric columns of the US dataframe
df_us.describe()

#what 5 years had F5 caused the most deaths in the US
df_us.groupby('Year')['Deaths'].sum().sort_values(ascending=False).head(5)

#what are the top 5 months when F5 caused the most deaths in the US
df_us.groupby('Month')['Deaths'].sum().sort_values(ascending=False).head(5)

#what three months are F5 tornadoes more common in the US, order from most common to least common
df_us['Month'].value_counts().head(3)

#what month are F5 tornadoes more common outside the US
df_non_us['Month'].value_counts().head(1)

# what state has seen the most deaths due to F5 tornadoes
df_us.groupby('Loc')['Deaths'].sum().sort_values(ascending=False).head(5)

# what four states have seen the most F5 tornadoes
df_us['Loc'].value_counts().head(4)

# what country outside the US has seen the most deaths
df_non_us.groupby('Loc')['Deaths'].sum().sort_values(ascending=False).head(5)

# List the top three years when the US had the most F5 tornadoes
df_us['Year'].value_counts().head(3)

#on average, how many people are killed by an F5 tornado in the US
df_us['Deaths'].mean()
