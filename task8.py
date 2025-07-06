import pandas as pd

# Load the dataset 
df = pd.read_csv("Superstore.csv", encoding='cp1252')

# Display first few rows
print(df.head())

# Check basic info
print(df.info())

# Check for null values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Check unique values in 'Category' column
print(df_cleaned['Category'].unique())

# Convert 'Order Date' and 'Ship Date' to datetime
df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Order Date'], errors='coerce')
df_cleaned['Ship Date'] = pd.to_datetime(df_cleaned['Ship Date'], errors='coerce')

# Drop rows where date conversion failed
df_cleaned = df_cleaned.dropna(subset=['Order Date', 'Ship Date'])

# Save to new CSV
df_cleaned.to_csv("Superstore_Cleaned.csv", index=False)

print("Cleaned data saved successfully!")
