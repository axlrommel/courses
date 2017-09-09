import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MO2012Dem = pd.read_csv('ACS_12_5YR_S1701_with_ann.csv', index_col=0)
MO2013Dem = pd.read_csv('ACS_13_5YR_S1701_with_ann.csv', index_col=0)
MO2014Dem = pd.read_csv('ACS_14_5YR_S1701_with_ann.csv', index_col=0)
MO2015Dem = pd.read_csv('ACS_15_5YR_S1701_with_ann.csv', index_col=0)

col2012 = ['HC03_EST_VC01'
,'HC03_EST_VC09'
,'HC03_EST_VC10'
,'HC03_EST_VC14'
,'HC03_EST_VC15'
,'HC03_EST_VC22'
,'HC03_EST_VC23'
,'HC03_EST_VC28'
,'HC03_EST_VC29'
,'HC03_EST_VC30'
,'HC03_EST_VC31']

col2013_2014 = ['HC03_EST_VC01'
,'HC03_EST_VC09'
,'HC03_EST_VC10'
,'HC03_EST_VC14'
,'HC03_EST_VC15'
,'HC03_EST_VC22'
,'HC03_EST_VC23'
,'HC03_EST_VC27'
,'HC03_EST_VC28'
,'HC03_EST_VC29'
,'HC03_EST_VC30']

col2015 = ['HC03_EST_VC01'
,'HC03_EST_VC14'
,'HC03_EST_VC15'
,'HC03_EST_VC18'
,'HC03_EST_VC19'
,'HC03_EST_VC26'
,'HC03_EST_VC27'
,'HC03_EST_VC31'
,'HC03_EST_VC32'
,'HC03_EST_VC33'
,'HC03_EST_VC34']

df2012 = MO2012Dem[col2012]
df2013 = MO2013Dem[col2013_2014]
df2014 = MO2014Dem[col2013_2014]
df2015 = MO2015Dem[col2015]

colNames = ['Total','Male','Female','Race White','Race Black','Hispanic','White Non-Hispanic',
    'Less than HighSchool','High School Grad','Some College','College grad']

df2012.columns = colNames
df2013.columns = colNames
df2014.columns = colNames
df2015.columns = colNames

frames = [df2012,df2013,df2014,df2015]
result = pd.concat(frames)

moUnemploy = pd.read_excel('SeriesReport-20170908225834_e53e00.xlsx', skiprows = [10], header = 9)
moUnemploy = moUnemploy.set_index(['Year'])
moUnemploy['unemployment rate'] = moUnemploy[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']].mean(axis=1)
moUnemploy = moUnemploy[['unemployment rate']]
MOMerge = result.merge(moUnemploy, how='inner', left_index=True, right_index = True)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 9,
        }

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.text(3,3,'Overall Poverty in Missouri vs. \nUnemployment Rates')

l1, = axes[0,0].plot(MOMerge.index, MOMerge['unemployment rate'],label = 'unemployment rate')
l2, = axes[0,0].plot(MOMerge.index, MOMerge['Total'],label = 'total poverty')
# l1.set_label('unemployment rate')

l3 = axes[0,1].plot(MOMerge.index, MOMerge['unemployment rate'],label = 'unemployment rate')
l4 = axes[0,1].plot(MOMerge.index, MOMerge['Male'],label = 'Male')
l5 = axes[0,1].plot(MOMerge.index, MOMerge['Female'],label = 'Female')

l6 = axes[1,0].plot(MOMerge.index, MOMerge['unemployment rate'],label = 'unemployment rate')
l7 = axes[1,0].plot(MOMerge.index, MOMerge['Race White'],label = 'Race White')
l8 = axes[1,0].plot(MOMerge.index, MOMerge['Race Black'],label = 'Race Black')
l9 = axes[1,0].plot(MOMerge.index, MOMerge['Hispanic'],label = 'Hispanic')

l10 = axes[1,1].plot(MOMerge.index, MOMerge['unemployment rate'],label = 'unemployment rate')
l11 = axes[1,1].plot(MOMerge.index, MOMerge['Less than HighSchool'],label = 'Less than HighSchool')
l12 = axes[1,1].plot(MOMerge.index, MOMerge['High School Grad'],label = 'High School Grad')
l13 = axes[1,1].plot(MOMerge.index, MOMerge['Some College'],label = 'Some College')
l14 = axes[1,1].plot(MOMerge.index, MOMerge['College grad'],label = 'College grad')

axes[0,0].set_ylabel('%',font)
axes[1,0].set_ylabel('%',font)
axes[1,0].set_xlabel('Year',font)
axes[1,1].set_xlabel('Year',font)
axes[0,0].set_title('Overall Poverty',font)
axes[0,1].set_title('By Sex',font)
axes[1,0].set_title('By Race',font)
axes[1,1].set_title('By Education level',font)
axes[0,0].set_yticks([6,8,10,12,14,16])
axes[0,1].set_yticks([6,9,12,15])
axes[1,0].set_yticks([5,10,15,20,25,30])
axes[1,1].set_yticks([5,10,15,20,25])
plt.setp([a.get_xticklabels() for a in axes[0, :]], visible=False)
plt.show()