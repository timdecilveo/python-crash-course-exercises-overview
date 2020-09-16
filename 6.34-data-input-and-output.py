import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# pip3 install sqlalchemy lxml html5lib beautifulsoup4
df = pd.read_csv(r".\udemy\python-for-data-science-and-machine-learning-bootcamp\06\example.csv")
print(df)
print(f"--------------------------------------------------------")

#.to_csv() - allows you to write to a CSV file
index_update = df.to_csv('My_ouput',index=False)
print(f"index_update:")
print(df)
print(f"--------------------------------------------------------")

# for Excel, you must pass in the sheet name
df_xlsx = pd.read_excel(r".\udemy\python-for-data-science-and-machine-learning-bootcamp\06\Excel_Sample.xlsx", sheet_name='Sheet1')
print(df_xlsx)
print(f"--------------------------------------------------------")

# writing to and creating a new excel file
def df_xlsx_write():
    # pip3 install openpyxl
    return df.to_excel(r".\udemy\python-for-data-science-and-machine-learning-bootcamp\06\Excel_Sample2.xlsx", sheet_name='NewSheet')
df_xlsx_write()
print(f"--------------------------------------------------------")

# web scraping with pandas
fdic_link = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
data = pd.read_html(fdic_link)
print(data)
print(type(data))
print(f"--------------------------------------------------------")

print(data[0])
print(f"--------------------------------------------------------")

print(data[0].head())
print(f"--------------------------------------------------------")

# SQL
engine = create_engine('sqlite:///:memory:')
#print(df.to_sql('my_table', engine))
def sql_engine():
    df.to_sql('my_table', engine)
    sqldf = pd.read_sql('my_table', con=engine)
    return sqldf
print(sql_engine())





