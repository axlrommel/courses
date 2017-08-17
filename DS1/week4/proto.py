import pandas as pd
houseP = pd.read_csv('City_Zhvi_AllHomes.csv', index_col=0)

columns_to_keep = []
for i in range(2000, 2017):
    year = str(i)
    houseP[year + 'q1'] = houseP[[year + '-01',year + '-02',year + '-03']].mean(axis=1)
    houseP[year + 'q2'] = houseP[[year + '-04',year + '-05',year + '-06']].mean(axis=1)
    houseP[year + 'q3'] = houseP[[year + '-07',year + '-08',year + '-09']].mean(axis=1)
    houseP[year + 'q4'] = houseP[[year + '-10',year + '-11',year + '-12']].mean(axis=1)
    columns_to_keep.append(year + 'q1')
    columns_to_keep.append(year + 'q2')
    columns_to_keep.append(year + 'q3')
    columns_to_keep.append(year + 'q4')

columns_to_keep.pop(len(columns_to_keep)-1) #remove 2016q4
houseP.set_index(['State','RegionName'],inplace=True)
df = houseP[columns_to_keep]
print(df.tail)




