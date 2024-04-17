import pandas as pd
# Read data from CSV into DataFrame:
df = pd.read_csv("Website Access Data.csv")
# List of column names containing inconsistent formatting:
inconsistent_formats = ['column5']
# Handle inconsistent formatting for each column:
for column in inconsistent_formats:
    df[column] = pd.to_datetime(df[column], format="%d/%m/%Y") # Convert to dd/mm/yyyy format
# Check the format of the columns in the DataFrame:
print(df.dtypes)
# Save the converted DataFrame to a new CSV file:
df.to_csv("data_formatted.csv", index=False)