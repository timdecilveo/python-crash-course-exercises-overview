# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())
print("-------------------------")

#sns.scatterplot(x='sex', y='total_bill', data=tips)
#sns.countplot(x='sex', data=tips)
#sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
#sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
#sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

# For .swarmplot(), you can plot the different days of the week and the price movements on a percentage basis
#sns.swarmplot(x='day', y='total_bill', data=tips)

#sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')







plt.show()