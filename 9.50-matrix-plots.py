# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print('tips:')
print(tips.head())
print("flights:")
print(flights.head())

tc = tips.corr()
print('tc')
print(tc)

#sns.heatmap(tc, annot=True, cmap='coolwarm')

fp= flights.pivot_table(index='month', columns='year', values='passengers')
#print(fp)
#sns.heatmap(fp, linecolor='white', linewidths=1)
sns.clustermap(fp)







plt.show()