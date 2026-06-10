import pandas as pd
import numpy as np


data = {
    'OrderID': range(1, 101),
    'Product_Segment': np.random.choice(['Electronics', 'Clothing', 'Home Appliances'], 100),
    'Sales': np.random.randint(100, 5000, 100),
    'Profit': np.random.randint(-500, 1500, 100),
    'Region': np.random.choice(['North', 'East', 'West', 'South'], 100),
    'Order_Date': pd.date_range(start='2026-01-01', periods=100, freq='D')
}
df = pd.DataFrame(data)


df.loc[df['Sales'] > 4500, 'Sales'] = np.nan 

print("--- PEHLE 5 ROWS ---")
print(df.head())


sales_median = df['Sales'].median()
df['Sales'] = df['Sales'].fillna(sales_median)


df.to_csv('Cleaned_Sales_Data.csv', index=False)
print("\nCleaned file 'Cleaned_Sales_Data.csv' file saved!")