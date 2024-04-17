import pandas as pd

# Read the customer data from the CSV file into a DataFrame
df = pd.read_csv("Customer Data.csv")

# Display information about missing data in the DataFrame
print("Missing data information:")
print(df.isnull().sum())

# Handle missing data
# Fill the missing values in the 'Age' column with the mean value
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill the missing values in the 'Country' column with 'Unknown'
df['Country'].fillna('Unknown', inplace=True)

# Display the DataFrame after handling missing data
print("\nDataFrame after handling missing data:")
print(df)