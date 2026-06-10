import pandas as pd
import numpy as np

# 1. Generate synthetic customer dataset for analysis
np.random.seed(42)
customer_data = {
    'CustomerID': range(1001, 1101),
    'Age': np.random.randint(18, 60, 100),
    'Annual_Income_k': np.random.randint(15, 100, 100),
    'Spending_Score': np.random.randint(1, 100, 100)
}
df_cust = pd.DataFrame(customer_data)

print("--- FIRST 5 CUSTOMER RECORDS ---")
print(df_cust.head())

# 2. Customer Segmentation Logic (Resume Point 1)
# Categorizing customers into strategic cohorts based on income and spending patterns
def assign_segment(row):
    if row['Spending_Score'] > 70 and row['Annual_Income_k'] > 50:
        return 'High-Value VIP'
    elif row['Spending_Score'] < 40:
        return 'Low-Value / At-Risk'
    else:
        return 'Average / Potential'

df_cust['Customer_Segment'] = df_cust.apply(assign_segment, axis=1)

print("\n--- CUSTOMER COUNT PER SEGMENT ---")
print(df_cust['Customer_Segment'].value_counts())

# 3. Export the final segmented model output to a CSV file (Resume Point 3)
df_cust.to_csv('Customer_Segments_Output.csv', index=False)
print("\nSuccess! Final model output 'Customer_Segments_Output.csv' has been saved.")