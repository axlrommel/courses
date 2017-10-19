import pandas as pd

df1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_costliest_Atlantic_hurricanes')
df = df1[0].drop(df1[0].index[0]).drop(5, axis=1)
df.columns = ['Name','Cost in Billions','Season','Classification','Areas Affected']
df['Classification']=df['Classification'].apply(lambda x: str(x)[3:]).apply(lambda x: x.strip())
df['Cost in Billions']=df['Cost in Billions'].apply(lambda x: str(x)[1:]).apply(pd.to_numeric)
df.at[34,'Classification']='Category 2 hurricane'
df.at[35,'Classification']='Category 2 hurricane'
df.at[45,'Classification']='Category 2 hurricane'

df.sort_values(['Cost in Billions'], ascending = False).head(10)
df['Season'].value_counts().head(4)
df[df['Areas Affected'].str.contains("Florida")]['Cost in Billions'].sum()
df[df['Areas Affected'].str.contains("Texas")]['Cost in Billions'].sum()
df[df['Areas Affected'].str.contains("Cuba")]['Cost in Billions'].sum()
df[df['Areas Affected'].str.contains("Louisiana")]['Cost in Billions'].sum()
df.groupby('Classification')['Cost in Billions'].sum().sort_values(ascending=False)
df.groupby('Season')['Cost in Billions'].sum().sort_values(ascending=False).head(8)
