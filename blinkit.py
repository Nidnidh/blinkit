import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("blinkit_data.csv")
np.random.seed(42)
df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat',
                                                         'low fat' : 'Low Fat',
                                                         'reg' : 'Regular'})
df.head()

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
number_of_items = df['Sales'].count()
average_rating = df['Rating'].mean()

print(total_sales)
print(average_sales)
print(number_of_items)
print(average_rating)

sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()
sales_by_item = (
    df.groupby('Item Type')['Sales'].sum().sort_values(ascending=True)
)
sales_by_year = (
    df.groupby('Outlet Establishment Year')['Sales']
    .sum()
    .sort_index()
)
print(sales_by_fat)
print(sales_by_item)
print(sales_by_year)

sales_by_item.plot(kind='bar', title='Item Type')
plt.ylabel('Item Type')
plt.xlabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sales_by_fat.plot(kind='pie', title='Sales By Fat Content')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sales_by_year.plot(kind='line', title='Sales By Fat Content')
plt.xlabel('Outline Establishment Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()