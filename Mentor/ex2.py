import pandas as pd

df1 = pd.read_html('https://en.wikipedia.org/wiki/Sales_taxes_in_the_United_States')
df = df1[3].drop(df1[3].index[0]).drop([3,4,5,6,7,8], axis=1)
df.columns = ['State/territory/district'  ,'Base sales tax'  ,'Total with max local surtax']

#remove the % sign
df['Base sales tax']=df['Base sales tax'].apply(lambda x: str(x)[:-1]).apply(pd.to_numeric)
df['Total with max local surtax']=df['Total with max local surtax'].apply(lambda x: str(x)[:-1]).apply(pd.to_numeric)

#find the state or territory with the highest Base sales tax
df.loc[df['Base sales tax'].idxmax()]['State/territory/district']

# find the state or territory with the highest Total with max local surtax
df.loc[df['Total with max local surtax'].idxmax()]

# return a numpy array of states and territories with a zero percent base sales tax
pd.Series(df.loc[df['Base sales tax'] == 0]['State/territory/district']).values

# which state or territory has the lowest non-zero percent base sales tax
#tip: create a temporary dataframe and remove from it the rows with a zero percent base sales tax
# and then get the state or territory with the lowest tax
data = df
mask = data['Base sales tax']== 0 #should return an array of true/false
dq = data[~mask] # remove the falses
dq.loc[dq['Base sales tax'].idxmin()]['State/territory/district']