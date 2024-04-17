import pandas as pd
from sklearn import preprocessing

# Read the dataset from CSV
df = pd.read_csv("Product Data.csv")
# Fix the Normalizing and Scaling errors
# Normalization
df['Price (million VND)'] = (df['Price (million VND)'] - df['Price (million VND)'].min()) / (df['Price (million VND)'].max() - df['Price (million VND)'].min())
df['Quantity'] = (df['Quantity'] - df['Quantity'].min()) / (df['Quantity'].max() - df['Quantity'].min())
# Scaling
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
df[['Price (million VND)', 'Quantity']] = scaler.fit_transform(df[['Price (million VND)', 'Quantity']])

# Print the fixed dataset
print(df)