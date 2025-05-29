import pandas as pd
import numpy as np

# Load the dataset
data_path = '/home/ubuntu/Downloads/USA-Housing-Dataset.csv'
df = pd.read_csv(data_path)

# Display basic information about the dataset
print("Original Dataset Info:")
df.info()

print("\nOriginal Missing Values:")
print(df.isnull().sum())

# --- Data Cleaning and Preprocessing ---

# 1. Drop irrelevant columns
# 'Unnamed: 0' and 'id' are identifiers. 'date' requires time-series processing, which is complex for simple regression.
# 'zipcode' could be treated as categorical, but adds complexity. We'll drop these for now.
df_processed = df.drop(['Unnamed: 0', 'id', 'date', 'zipcode'], axis=1)
print("\nColumns after dropping irrelevant ones:", df_processed.columns)

# 2. Handle Missing Values
# Impute missing 'bedrooms' and 'bathrooms' with their respective medians
bedrooms_median = df_processed['bedrooms'].median()
bathrooms_median = df_processed['bathrooms'].median()
df_processed['bedrooms'].fillna(bedrooms_median, inplace=True)
df_processed['bathrooms'].fillna(bathrooms_median, inplace=True)

print("\nMissing Values after Imputation:")
print(df_processed.isnull().sum())

# 3. Verify Target Variable and Separate Features/Target
# Use the correct column name 'price' (lowercase)
target_column = 'price'

if target_column not in df_processed.columns:
    print(f"\nError: '{target_column}' column not found. Please verify the target variable name.")
    # Exit or handle appropriately
else:
    X = df_processed.drop(target_column, axis=1)
    y = df_processed[target_column]

    print("\nFeatures (X) columns:")
    print(X.columns)
    print("\nTarget (y) head:")
    print(y.head())

    # Save the processed features and target for the next step
    X.to_csv('/home/ubuntu/features_processed.csv', index=False)
    y.to_csv('/home/ubuntu/target_processed.csv', index=False, header=True)

    print("\nData loaded, cleaned, preprocessed, and saved.")
    print(f"Shape of features (X): {X.shape}")
    print(f"Shape of target (y): {y.shape}")


