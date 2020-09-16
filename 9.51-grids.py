# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())
tips = sns.load_dataset('tips')
print(tips.head())

# .PairGrid() allows you to plot different kinds of plots on a big grid of plots
g = sns.PairGrid(iris)
#g.map_diag(sns.distplot)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)

# .FacetGrid(data, col, row)
h = sns.FacetGrid(data=tips, col='time', row='smoker')
#h.map(sns.distplot, 'total_bill')
#h.map(plt.scatter, 'total_bill', 'tip')

plt.show()