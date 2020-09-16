# Ecommerce Purchases Exercise
# In this Exercise you will be given some Fake Data about some purchases done through Amazon!
# Just go ahead and follow the directions and try your best to answer the questions and complete the tasks.
# Feel free to reference the solutions. Most of the tasks can be solved in different ways.
# For the most part, the questions get progressively harder.

# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# Also note that all of these questions can be answered with one line of code.

# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **
import pandas as pd

df = pd.read_csv(r".\udemy\python-for-data-science-and-machine-learning-bootcamp\07\Ecommerce Purchases.csv")
print(f"df:")
print(f"{df}")
print(f"---------------------------------------------------------")

# Check the head of the DataFrame.
print(f"df.head():")
print(f"{df.head()}")
print(f"---------------------------------------------------------")

# ** How many rows and columns are there? **
print(f"df.info():")
print(f"{df.info()}")
print(f"---------------------------------------------------------")

# ** What is the average Purchase Price? **
print(f"df['Purchase Price'].mean():")
print(f"{df['Purchase Price'].mean()}")
print(f"---------------------------------------------------------")

# ** What were the highest and lowest purchase prices? **
print(f"df['Purchase Price'].max():")
print(f"{df['Purchase Price'].max()}")
print(f"df['Purchase Price'].min():")
print(f"{df['Purchase Price'].min()}")
print(f"---------------------------------------------------------")

# ** How many people have English 'en' as their Language of choice on the website? **
print(f"sum(df['Language'] == 'en'):")
print(f"{sum(df['Language'] == 'en')}")
#print(f"{df[df['Language'] == 'en'].count()}")
print(f"---------------------------------------------------------")

# ** How many people have the job title of "Lawyer" ? **
print(f"sum(df['Job'] == 'Lawyer'):")
print(f"{sum(df['Job'] == 'Lawyer')}")
#print(f"{df[df['Job'] == 'Lawyer'].count()}")
print(f"---------------------------------------------------------")

# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
print(f"sum(df['AM or PM'] == 'AM'):")
print(f"{sum(df['AM or PM'] == 'AM')}")
print(f"sum(df['AM or PM'] == 'PM'):")
print(f"{sum(df['AM or PM'] == 'PM')}")
print(f"{df['AM or PM'].value_counts()}")
print(f"---------------------------------------------------------")

# ** What are the 5 most common Job Titles? **
print(f"df['Job'].value_counts().head(5):")
print(f"{df['Job'].value_counts().head(5)}")
print(f"---------------------------------------------------------")

# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **
print(f"df[df['Lot'] == '90 WT']['Purchase Price']:")
print(f"{df[df['Lot'] == '90 WT']['Purchase Price']}")
print(f"---------------------------------------------------------")

# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **
print(f"df[df['Credit Card'] == 4926535242672853]['Email']:")
print(f"{df[df['Credit Card'] == 4926535242672853]['Email']}")
print(f"---------------------------------------------------------")

# * How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?**
print(f"df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)].count():")
print(f"{df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)].count()}")
print(f"---------------------------------------------------------")

# ** Hard: How many people have a credit card that expires in 2025? **
print(f"sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25'):")
print(f"{sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25')}")
print(f"---------------------------------------------------------")

# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **
print(f"df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5):")
print(f"{df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)}")
print(f"---------------------------------------------------------")