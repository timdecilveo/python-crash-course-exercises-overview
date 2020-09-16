# https://seaborn.pydata.org/ - documentation
# pip3 install seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn Exercises
#Time to practice your new seaborn skills!
#Try to recreate the plots below (don't worry about color schemes, just the plot itself).

#The Data
#We will be working with a famous titanic data set for these exercises.
#Later on in the Machine Learning section of the course, we will revisit this data,
#and use it to predict survival rates of passengers.
#For now, we'll just focus on the visualization of the data with seaborn:

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())

#Exercises
#** Recreate the plots below using the titanic dataframe.
# There are very few hints since most of the plots can be done with just
# one or two lines of code and a hint would basically give away the solution.
# Keep careful attention to the x and y labels for hints.**
#* *Note! In order to not lose the plot image,
# make sure you don't code in the cell that is directly above the plot,
# there is an extra cell above that one which won't overwrite that plot! **

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""sns.jointplot(x='fare', y='age', data=titanic)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""sns.distplot(titanic['fare'], bins=30,kde=False)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""sns.boxplot(x='class', y='age', data=titanic)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""sns.swarmplot(x='class', y='age', data=titanic)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""sns.countplot(x='sex', data=titanic)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
"""tc = titanic.corr()
sns.heatmap(tc)"""

# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!
g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')

#Great Job!
#That is it for now!
#We'll see a lot more of seaborn practice problems in the machine learning section!
plt.show()