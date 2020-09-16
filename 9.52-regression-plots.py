# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

#sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s':100})
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex', aspect=0.6, size=8)




plt.show()