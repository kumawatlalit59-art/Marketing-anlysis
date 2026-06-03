#load data 
import pandas as  pd

df= pd.read_csv("marketing.csv")
print(df.head())
print(df.isnull().sum())
df = df.dropna()

df['Date']= pd.to_datetime(df['Date'])
 
#Marketing trends anlyis 
monthly_sales = df.groupby(
    df['Date'].dt.month
)['Sales'].sum()

print(monthly_sales)

#channels
channel_sales = df.groupby(
    'channel'
)['Sales'].sum()

print(channel_sales)

#top products
top_products = df.groupby(
    'product'
)['sales'].sum().sort_values(
    ascending=False
)

print(top_products)


import pandas as pd 
import pyodbc

df = pd.read_csv("marketing.csv")

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-GB564FT;"
    "DATABASE=MarketingCV;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
      INSERT INTO MarketingData
      (CustomerID, Product, sales, Channel, SaleDate)
      VALUES (?, ?, ?, ?, ?)
    """,
    row['CustomerID'],
    row['Product'],
    row['Sales'],
    row['Channel'],
    row['SaleDate'])

conn.commit()
conn.close()

print("Data inserted successfully!")