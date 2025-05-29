import pandas as pd
from sklearn.model_selection import train_test_split

# Load the processed features and target
X = pd.read_csv("/home/ubuntu/features_processed.csv")
y = pd.read_csv("/home/ubuntu/target_processed.csv")["price"] # Ensure y is a Series

# Split the data into training and testing sets (80% train, 20% test)
# Use random_state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the resulting datasets
print(f"Shape of X_train: {X_train.shape}")
print(f"Shape of X_test: {X_test.shape}")
print(f"Shape of y_train: {y_train.shape}")
print(f"Shape of y_test: {y_test.shape}")

# Save the split data for the next steps (optional, but good practice)
X_train.to_csv("/home/ubuntu/X_train.csv", index=False)
X_test.to_csv("/home/ubuntu/X_test.csv", index=False)
y_train.to_csv("/home/ubuntu/y_train.csv", index=False, header=True)
y_test.to_csv("/home/ubuntu/y_test.csv", index=False, header=True)

print("\nData successfully split into training and testing sets and saved.")


