#Imports
#** Import pandas, numpy, matplotlib,and seaborn.
# Then set %matplotlib inline (You'll import sklearn as you need it.)**
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# ** Read in the Ecommerce Customers csv file as a DataFrame called customers.**
df = pd.read_csv(r'.\udemy\python-for-data-science-and-machine-learning-bootcamp\15\Ecommerce Customers.csv')
# Check the head of customers, and check out its info() and describe() methods.
print(df.head())
print("-------------------------------------")
print(df.info())
print("-------------------------------------")
print(df.describe())
print("-------------------------------------")
print(df.columns)
print("-------------------------------------")

# Exploratory Data Analysis
# Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.
# Does the correlation make sense?
#sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)
#plt.show()

# ** Do the same but with the Time on App column instead. **
#sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)
#plt.show()

# ** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**
#sns.jointplot(x='Time on App', y='Length of Membership', data=df, kind='hex', color='#4CB391')
#plt.show()

# Let's explore these types of relationships across the entire data set.
# Use pairplot to recreate the plot below.(Don't worry about the the colors)
#sns.pairplot(data=df)
#plt.show()

# Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
print('Length of membership')

# *Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership. *


# Training and Testing Data
# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# ** Set a variable X equal to the numerical features of the customers
# and a variable y equal to the "Yearly Amount Spent" column. **
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# ** Use model_selection.train_test_split from sklearn to split the data into training and testing sets.
# Set test_size=0.3 and random_state=101**
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

# Create an instance of a LinearRegression() model named lm.
lm = LinearRegression()

# ** Train/fit lm on the training data.**
lm.fit(X_train, y_train)
print(lm.fit(X_train, y_train))
print("-------------------------------------")
print(f"Intercept: {lm.intercept_}")
print("-------------------------------------")

# Print out the coefficients of the model
print(f"Coefficients: {lm.coef_}")
print("-------------------------------------")

# Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
# ** Use lm.predict() to predict off the X_test set of the data.**
predictions = lm.predict(X_test)
print(f"Predictions: {predictions}")
print("-------------------------------------")

# ** Create a scatterplot of the real test values versus the predicted values. **
#plt.scatter(y_test, predictions)

# Evaluating the Model
# Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).
# ** Calculate the Mean Absolute Error,
# Mean Absolute Error (MAE)
mae = metrics.mean_absolute_error(y_test, predictions)
print(f"MAE: {mae}")

# Mean Squared Error
mse = metrics.mean_squared_error(y_test, predictions)
print(f"MSE: {mse}")

# and the Root Mean Squared Error
# Root Mean Squared Error(RMSE)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse}")
print("-------------------------------------")

# Residuals
# You should have gotten a very good model with a good fit.
# Let's quickly explore the residuals to make sure everything was okay with our data.
# Plot a histogram of the residuals and make sure it looks normally distributed.
# Use either seaborn distplot, or just plt.hist().
sns.distplot((y_test - predictions))

# Conclusion
# We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development?
# Or maybe that doesn't even really matter, and Membership Time is what is really important.
# Let's see if we can interpret the coefficients at all to get an idea.

# ** Recreate the dataframe below. **
cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
print(cdf)

# ** How can you interpret these coefficients? **
# Answer here

# Do you think the company should focus more on their mobile app or on their website?
print("Mobile")
# Answer here
plt.show()