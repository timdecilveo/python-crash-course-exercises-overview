# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution Plots
tips = sns.load_dataset('tips')

#sns.distplot(tips['total_bill'], bins=30)
#sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
sns.pairplot(tips, hue='sex')
sns.rugplot(tips['total_bill'])

# always use plt.show()
plt.show()
