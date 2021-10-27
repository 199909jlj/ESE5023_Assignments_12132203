# -*- coding: utf-8 -*-

# 1.direction angle : 001~360 Angular Degrees 999 = Missing. If type code (below) = V, then 999 indicates variable wind direction.
# 2.direction quality code : 
    #0 = Passed gross limits check
    #1 = Passed all quality control checks
    #2 = Suspect
    #3 = Erroneous
    #4 = Passed gross limits check, data originate from an NCEI data source
    #5 = Passed all quality control checks, data originate from an NCEI data source
    #6 = Suspect, data originate from an NCEI data source
    #7 = Erroneous, data originate from an NCEI data source
    #9 = Passed gross limits check if element is present
# 3.type code : 
    #A = Abridged Beaufort
    #B = Beaufort
    #C = Calm
    #H = 5-Minute Average Speed
    #N = Normal
    #R = 60-Minute Average Speed
    #Q = Squall
    #T = 180 Minute Average Speed
    #V = Variable
    #9 = Missing
# 4.speed rate : 0~900 m/s 9999 = Missing
# 5.speed quality code :
    #0 = Passed gross limits check
    #1 = Passed all quality control checks
    #2 = Suspect
    #3 = Erroneous
    #4 = Passed gross limits check, data originate from an NCEI data source
    #5 = Passed all quality control checks, data originate from an NCEI data source
    #6 = Suspect, data originate from an NCEI data source
    #7 = Erroneous, data originate from an NCEI data source
    #9 = Passed gross limits check if element is present
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/ASUS/Desktop/ESS5023 Assigment/2281305.csv')
data = data[['DATE','WND']]
data['MONTH'] = pd.to_datetime(data['DATE']).dt.month
data['YEAR'] = pd.to_datetime(data['DATE']).dt.year
a = data['WND'].str.split(',', expand = True)
a['DATE'] = data['DATE']
data = pd.merge(data,a,on='DATE')
data = data[['YEAR','MONTH',3]]
data.rename(columns={3:'SPEEDRATE'},inplace=True)
data['SPEEDRATE'] = data['SPEEDRATE'].apply(int)
data.groupby(['YEAR','MONTH']).mean().plot()