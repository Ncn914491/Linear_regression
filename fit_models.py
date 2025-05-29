import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the training data
X_train = pd.read_csv("/home/ubuntu/X_train.csv")
y_train = pd.read_csv("/home/ubuntu/y_train.csv")["price"] # Ensure y_train is a Series

# --- Simple Linear Regression ---
# Choose a single feature (e.g., sqft_living)
simple_feature = 'sqft_living'
print(f"\n--- Fitting Simple Linear Regression (Feature: {simple_feature}) ---")

# Reshape X_train for a single feature
X_train_simple = X_train[[simple_feature]]

# Initialize and fit the model
simple_lr_model = LinearRegression()
simple_lr_model.fit(X_train_simple, y_train)

# Save the simple model
joblib.dump(simple_lr_model, '/home/ubuntu/simple_linear_regression_model.joblib')
print("Simple Linear Regression model fitted and saved.")
print(f"Coefficient: {simple_lr_model.coef_[0]}")
print(f"Intercept: {simple_lr_model.intercept_}")

# --- Multiple Linear Regression ---
print("\n--- Fitting Multiple Linear Regression (All Features) ---")

# Initialize and fit the model
multiple_lr_model = LinearRegression()
multiple_lr_model.fit(X_train, y_train)

# Save the multiple model
joblib.dump(multiple_lr_model, '/home/ubuntu/multiple_linear_regression_model.joblib')
print("Multiple Linear Regression model fitted and saved.")
print("Coefficients:")
# Create a Series for better readability of coefficients
coeffs = pd.Series(multiple_lr_model.coef_, index=X_train.columns)
print(coeffs)
print(f"\nIntercept: {multiple_lr_model.intercept_}")


