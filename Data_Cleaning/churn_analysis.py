import pandas as pd
import matplotlib.pyplot as plt

# Dataset load करणे
df = pd.read_csv("customer_data.csv")

print("Customer Data:")
print(df.head())

# Basic information
print("\nDataset Information:")
print(df.info())

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Churn count
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Churn percentage
print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# Churn by Login Frequency
print("\nChurn by Login Frequency:")
print(pd.crosstab(df["LoginFrequency"], df["Churn"]))

# Churn by Usage
print("\nChurn by Usage:")
print(pd.crosstab(df["Usage"], df["Churn"]))

# Churn by Support Calls
print("\nChurn by Support Calls:")
print(pd.crosstab(df["SupportCalls"], df["Churn"]))

# Churn by Tenure
print("\nChurn by Tenure:")
print(pd.crosstab(df["Tenure"], df["Churn"]))

# Churn graph
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Analysis")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()