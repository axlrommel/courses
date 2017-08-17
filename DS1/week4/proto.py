import pandas as pd
houseP = pd.read_csv('City_Zhvi_AllHomes.csv', index_col=0)
# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
houseP['State'].replace(states,inplace=True)
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
print(df.loc["Texas"].loc["Austin"].loc["2010q3"])
#print(df.tail)




