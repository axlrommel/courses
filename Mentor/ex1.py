import pandas as pd

df1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_costliest_Atlantic_hurricanes')
df = df1[0].drop(df1[0].index[0]).drop(5, axis=1)
df.columns = ['Name','Cost in Billions','Season','Classification','Areas Affected']
df['Classification']=df['Classification'].apply(lambda x: str(x)[3:]).apply(lambda x: x.strip()).replace('\xa0',' ',regex=True)
df['Cost in Billions']=df['Cost in Billions'].apply(lambda x: str(x)[1:]).apply(pd.to_numeric)

# list the 10 most costly hurricanes and their season
# should return a dataframe with two columns: the name of the hurricane and the season
df.sort_values(['Cost in Billions'], ascending = False).head(10)[['Name','Season']]

# find the four seasons with the most hurricanes on this list, 
# return a dataset of size 4 with an index of 
# season, and a value of number of hurricanes for that season:
# e.g
# 2005  6
# 2012  2
# ...  
df['Season'].value_counts().head(4)

# compare the cost of the damage caused by the hurricanes for Florida, 
# Texas and Louisiana.
# return a tuple with the three states in order from more cost sustained
# by hurricane damage to less cost sustained
# e.g ('Louisiana','Texas','Florida')
df[df['Areas Affected'].str.contains("Florida")]['Cost in Billions'].sum()
df[df['Areas Affected'].str.contains("Texas")]['Cost in Billions'].sum()
df[df['Areas Affected'].str.contains("Louisiana")]['Cost in Billions'].sum()

#List the four seasons which were most costly along with its associated cost
#put your results in a series where the index is the season and the value is the cost
df.groupby('Season')['Cost in Billions'].sum().sort_values(ascending=False).head(4)

# How much more costly were hurricanes of category 5 than hurricanes of category 4
# you result should be a single number representing the difference in billions
se = df.groupby('Classification')['Cost in Billions'].sum()
se.loc['Category 5 hurricane'] - se.loc['Category 4 hurricane']
