import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# Compute the total number of deaths caused by earthquakes since 2150 B.C. in each country, 
# and then print the top ten countries along with the total number of deaths.
data = pd.read_csv('C:/Users/ASUS/Desktop/ESS5023 Assigment/Sig_Eqs.csv')
data1 = data[['Country','Deaths']]
print(data1.groupby(['Country']).sum().sort_values('Deaths',ascending=False).iloc[0:10])

# Compute the total number of earthquakes with magnitude larger than 6.0 
# (use column Mag as the magnitude) worldwide each year, 
# and then plot the time series. Do you observe any trend? Explain why or why not?
data2 = data[['Year','Mag']].loc[data['Mag']>6.0]
data2.groupby('Year').count()['Mag'].plot()
plt.legend()

# Write a function CountEq_LargestEq that returns both (1) the total number of earthquakes since 2150 B.C. 
# in a given country AND (2) the date of the largest earthquake ever happened in this country.
# Apply CountEq_LargestEq to every country in the file, report your results in a descending order.
def CountEq_LargestEq(a): 
    data3 = data.loc[data['Country']==a]
    a = len(data3)
    b= data['Year'].iloc[data3['Mag'].idxmax()]
    print(a,int(b))
    
CountEq_LargestEq('CHINA')

