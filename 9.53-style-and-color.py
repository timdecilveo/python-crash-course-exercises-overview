# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

#sns.set_style('ticks')
#plt.figure(figsize=(12, 3))
#sns.set_context('paper')
#sns.countplot(x='sex', data=tips)
#sns.despine(left=True, bottom=True)

# colormaps: https://matplotlib.org/tutorials/colors/colormaps.html
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')

plt.show()