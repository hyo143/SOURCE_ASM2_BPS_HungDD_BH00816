import pandas as pd
# Read data from CSV file
df = pd.read_csv("Sales Data.csv")
# Check and handle outliers
df['Quantity'] = df['Quantity'].apply(lambda x: max(x, 0))  # Ensure non-negative quantity
# Print the processed data table
print(df)