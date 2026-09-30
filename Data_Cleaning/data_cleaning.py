import pandas as pd

df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# Duplicate rows remove
df = df.drop_duplicates()

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Missing values fill
df = df.fillna("Unknown")

# Text format consistent करणे
for column in df.select_dtypes(include="object"):
    df[column] = df[column].str.strip().str.title()

# Clean data save
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nData cleaning completed!")
