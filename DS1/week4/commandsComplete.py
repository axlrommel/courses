import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Definitions:
# A quarter is a specific three month period, Q1 is January through March, Q2 is April 
# through June, Q3 is July through September, Q4 is October through December.
# A recession is defined as starting with two consecutive quarters of GDP decline, 
# and ending with two consecutive quarters of GDP growth.
# A recession bottom is the quarter within a recession which had the lowest GDP.
# A university town is a city which has a high percentage of university students 
# compared to the total population of the city.
# Hypothesis: University towns have their mean housing prices less effected by 
# recessions. Run a t-test to compare the ratio of the mean price of houses in 
# university towns the quarter before the recession starts compared to the recession 
# bottom. (price_ratio=quarter_before_recession/recession_bottom)
# The following data files are available for this assignment:
# From the Zillow research data site (http://www.zillow.com/research/data/) 
# there is housing data for the United States. 
# In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv, 
# has median home sale prices at a fine grained level.
# From the Wikipedia page on college towns is a list of university towns in the 
# United States which has been copy and pasted into the file university_towns.txt.
# From Bureau of Economic Analysis, US Department of Commerce, the GDP 
# over time of the United States in current dollars (use the chained value in 2009 dollars), 
# in quarterly intervals, in the file gdplev.xls. For this assignment, 
# only look at GDP data from the first quarter of 2000 onward.

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
stateNames = states.values()
# '''Returns a DataFrame of towns and the states they are in from the university_towns.txt list. The format of the DataFrame should be:DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], columns=["State", "RegionName"]  )
def get_list_of_university_towns():
       
    # The following cleaning needs to be done:

    # 1. For "State", removing characters from "[" to the end.
    # 2. For "RegionName", when applicable, removing every character from " (" to the end.
    # 3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    import pandas as pd
    elements = []
    state = ""
    region = ""
    editStr = "[edit]"
    parens = " ("
    with open('university_towns.txt','r') as input:
        for line in input:
            editpos = line.find(editStr)
            parenspos = line.find(parens)
            if editpos > 0:
                state = line[:editpos]
            else :
                if parenspos > 0 :
                    region = line[:parenspos]
                else :
                    region = line.strip()
                elements.append([state,region])
    df = pd.DataFrame(elements,columns=['State', 'RegionName'])
    return df

def get_recession_start():
    # '''Returns the year and quarter of the recession start time as a 
    # string value in a format such as 2005q3'''
    gdp_df = pd.read_excel('gdplev.xls', skiprows = [6,7], parse_cols = "E,G", header = 5)
    gdp = gdp_df.iloc[212:] #read from row 212 onward

    prevGDP = 0
    gdpDecreasing = False
    quarterDepStarted = ""
    label = 'GDP in billions of chained 2009 dollars'
    for index, row in gdp.iterrows():
        if row[label] < prevGDP and gdpDecreasing == False:
            quarterDepStarted = index
            gdpDecreasing = True
        elif row[label] < prevGDP and gdpDecreasing == True:
            break
        else:
            gdpDecreasing = False
        prevGDP = row[label]

    return quarterDepStarted

def get_recession_end():
    # '''Returns the year and quarter of the recession end time as a 
    # string value in a format such as 2005q3'''
       
    import pandas as pd
    gdp_df = pd.read_excel('gdplev.xls', skiprows = [6,7], parse_cols = "E,G", header = 5)
    gdp = gdp_df.iloc[212:] #read from row 212 onward

    prevGDP = 0
    gdpIncreasing = False
    quarterDepEnded = ""
    label = 'GDP in billions of chained 2009 dollars'
    for index, row in gdp.iterrows():
        if index[:4] < '2009':
            continue
        elif row[label] > prevGDP and gdpIncreasing == False: 
            gdpIncreasing = True
        elif row[label] > prevGDP and gdpIncreasing == True:
            quarterDepEnded = index
            break
        else:
            gdpIncreasing = False
        prevGDP = row[label]

    return quarterDepEnded

def get_recession_bottom():
    # '''Returns the year and quarter of the recession bottom time as a 
    # string value in a format such as 2005q3'''
    gdp_df = pd.read_excel('gdplev.xls', skiprows = [6,7], parse_cols = "E,G", header = 5)
    gdp = gdp_df.iloc[212:] #read from row 212 onward

    prevGDP = 100000
    previndex = ""
    quarterDepBottom = ""
    label = 'GDP in billions of chained 2009 dollars'
    for index, row in gdp.iterrows():
        if index[:4] < '2009':
            continue
        elif row[label] > prevGDP:
            quarterDepBottom = previndex
            break
        prevGDP = row[label]
        previndex = index

    return quarterDepBottom


def convert_housing_data_to_quarters():
    # '''Converts the housing data to quarters and returns it as mean 
    # values in a dataframe. This dataframe should be a dataframe with
    # columns for 2000q1 through 2016q3, and should have a multi-index
    # in the shape of ["State","RegionName"].
    
    # Note: Quarters are defined in the assignment description, they are
    # not arbitrary three month periods.
    
    # The resulting dataframe should have 67 columns, and 10,730 rows.
    # '''
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
    print(df.loc["Texas"].loc["Austin"].loc["2010q3"]) #201966.666667
    return df

def run_ttest():
    # '''First creates new data showing the decline or growth of housing prices
    # between the recession start and the recession bottom. Then runs a ttest
    # comparing the university town values to the non-university towns values, 
    # return whether the alternative hypothesis (that the two groups are the same)
    # is true or not as well as the p-value of the confidence. 
    
   df['Price Ratio'] = df[recession_start].div(df[recession_bottom])

# the trick is to convert the 2 d list to a list of tuples before passing it to loc , using the tuple list you can find both uni and non-uni
    tuple_list = #convert ul to a list of tuples i.e [(State1,RegionName1),(State2,RegionName2),.....,(State517,RegionName517)]
    university_towns = hdf.loc[tuple_list]
    non_university_towns = hdf.loc[~hdf.index.isin(tuple_list)]

    # Return the tuple (different, p, better) where different=True if the t-test is
    # True at a p<0.01 (we reject the null hypothesis), or different=False if 
    # otherwise (we cannot reject the null hypothesis). The variable p should
    # be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    # value for better should be either "university town" or "non-university town"
    # depending on which has a lower mean price ratio (which is equivilent to a
    # reduced market loss).'''

import pandas as pd
import scipy as scipy
from scipy.stats import ttest_ind
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
hdf = houseP[columns_to_keep]

hdf['Price Ratio'] = hdf['2008q3'].div(hdf['2009q2'])

elements = []
state = ""
region = ""
editStr = "[edit]"
parens = " ("
with open('university_towns.txt','r') as input:
    for line in input:
        editpos = line.find(editStr)
        parenspos = line.find(parens)
        if editpos > 0:
            state = line[:editpos]
        else :
            if parenspos > 0 :
                region = line[:parenspos]
            else :
                region = line.strip()
            elements.append([state,region])

u_towns = hdf.loc[hdf.index.isin(elements)].dropna()['Price Ratio']
non_u_towns = hdf.loc[~hdf.index.isin(elements)].dropna()['Price Ratio']

(q,p) = scipy.stats.ttest_ind(u_towns, non_u_towns)

different = False
if p < 0.01:
    different = True

better = "university town"
if non_u_towns.mean() < u_towns.mean():
    better = "non-university town"

tup1 = (different,p, better)
print(tup1) 
    return "ANSWER"