import pandas as pd
import numpy as np

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
