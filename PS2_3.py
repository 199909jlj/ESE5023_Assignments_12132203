# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/ASUS/Desktop/ESS5023 Assigment/global_mean_md.csv')
data.groupby(['YYYY','MM']).mean()['CCl4'].plot()
plt.legend(['CCl4'])
print(data['CCl4'].describe())