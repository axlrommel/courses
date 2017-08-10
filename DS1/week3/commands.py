import pandas as pd
import numpy as np

energy = pd.read_csv('EnergyIndicators.csv', index_col=0)
energy = energy.replace('...',np.NaN)
energy.drop('Unnamed: 4', axis=1, inplace=True)
energy = energy.apply(pd.to_numeric, errors='ignore')


