import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from pandas_datareader import data, wb

# We need to get data using pandas datareader.
# We will get stock information for the following banks:
# Bank of America
# CitiGroup
# Goldman Sachs
# JPMorgan Chase
# Morgan Stanley
# Wells Fargo
# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks.
# Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol.
# This will involve a few steps:**

# Use datetime to set start and end datetime objects.
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)
# Figure out the ticker symbol for each bank.
# Figure out how to use datareader to grab info on the stock.
bac = data.DataReader("BAC", 'yahoo', start, end)
c = data.DataReader("C", 'yahoo', start, end)
gs = data.DataReader("GS", 'yahoo', start, end)
jpm = data.DataReader("JPM", 'yahoo', start, end)
ms = data.DataReader("MS", 'yahoo', start, end)
wfc = data.DataReader("WFC", 'yahoo', start, end)

data_frames = [bac, c, gs, jpm, ms, wfc]
print(data_frames)
print('**------------------**------------------**------------------**')
# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks.
# Set the keys argument equal to the tickers list.
# Also pay attention to what axis you concatenate on.**
bank_stocks = pd.concat(data_frames, keys=tickers, axis=1)
# ** Set the column name levels (this is filled out for you):**
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

print(bank_stocks.head())
print('**------------------**------------------**------------------**')

# ** What is the max Close price for each bank's stock throughout the time period?**
print(bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())
print('**------------------**------------------**------------------**')

# ** Create a new empty DataFrame called returns.
# This dataframe will contain the returns for each bank's stock returns are typically defined by:**
# # ** We can use pandas pct_change() method on the Close column to create a column representing this return value.
# Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.**
returns = pd.DataFrame()

for i in tickers:
    returns[i + ' Return'] = bank_stocks[i]['Close'].pct_change()
print(returns.head())
print('**------------------**------------------**------------------**')
# ** Create a pairplot using seaborn of the returns dataframe.
# What stock stands out to you?
# Can you figure out why?**
#sns.pairplot(returns[1:])
#plt.show()

# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns.
# You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?**
print(f"max return:\n{returns.idxmax()}")
print('**------------------**------------------**------------------**')

print(f"min return:\n{returns.idxmin()}")
print('**------------------**------------------**------------------**')

# ** Take a look at the standard deviation of the returns,
# which stock would you classify as the riskiest over the entire time period?
# Which would you classify as the riskiest for the year 2015?**
print(f"std:\n{returns.std()}")
print('**------------------**------------------**------------------**')

print(f"std 2015: {returns.loc['2015-01-01':'2015-12-31'].std()}")
print('**------------------**------------------**------------------**')

#** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **
#sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'], color='blue', bins=100)
#plt.show()
print('**------------------**------------------**------------------**')

# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **
#sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'], color='green', bins=100)
#plt.show()
print('**------------------**------------------**------------------**')

sns.set_style('whitegrid')
#bank_stocks.xs(key='Close', axis=1, level='Stock Info').plot()
#plt.show()

# Moving Averages
# Let's analyze the moving averages for these stocks in the year 2008.
# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**
#sns.lineplot(data=bank_stocks['BAC']['Close'].loc['2008-01-01':'2008-12-31'].rolling(window=30).mean(), color='blue')
#sns.lineplot(data=bank_stocks['BAC']['Close'].loc['2008-01-01':'2008-12-31'], color='green')
#plt.legend()
#plt.show()

# ** Create a heatmap of the correlation between the stocks Close Price.**
#sns.heatmap(data=bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
#plt.show()

# ** Optional: Use seaborn's clustermap to cluster the correlations together:**
#sns.clustermap(data=bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
#plt.show()


