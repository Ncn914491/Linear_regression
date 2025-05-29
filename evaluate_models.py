import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load the test data
X_test = pd.read_csv("/home/ubuntu/X_test.csv")
y_test = pd.read_csv("/home/ubuntu/y_test.csv")["price"] # Ensure y_test is a Series

# Load the saved models
simple_lr_model = joblib.load("/home/ubuntu/simple_linear_regression_model.joblib")
multiple_lr_model = joblib.load("/home/ubuntu/multiple_linear_regression_model.joblib")

# --- Evaluate Simple Linear Regression ---
simple_feature = 'sqft_living' # Must match the feature used in training
X_test_simple = X_test[[simple_feature]]
y_pred_simple = simple_lr_model.predict(X_test_simple)

print(f"\n--- Simple Linear Regression Evaluation (Feature: {simple_feature}) ---")
mae_simple = mean_absolute_error(y_test, y_pred_simple)
mse_simple = mean_squared_error(y_test, y_pred_simple)
rmse_simple = np.sqrt(mse_simple)
r2_simple = r2_score(y_test, y_pred_simple)

print(f"Mean Absolute Error (MAE): {mae_simple:.2f}")
print(f"Mean Squared Error (MSE): {mse_simple:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_simple:.2f}")
print(f"R-squared (R²): {r2_simple:.4f}")

# --- Evaluate Multiple Linear Regression ---
y_pred_multiple = multiple_lr_model.predict(X_test)

print("\n--- Multiple Linear Regression Evaluation (All Features) ---")
mae_multiple = mean_absolute_error(y_test, y_pred_multiple)
mse_multiple = mean_squared_error(y_test, y_pred_multiple)
rmse_multiple = np.sqrt(mse_multiple)
r2_multiple = r2_score(y_test, y_pred_multiple)

print(f"Mean Absolute Error (MAE): {mae_multiple:.2f}")
print(f"Mean Squared Error (MSE): {mse_multiple:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse_multiple:.2f}")
print(f"R-squared (R²): {r2_multiple:.4f}")

# Save evaluation results to a file (optional)
results = {
    "Simple_LR": {"MAE": mae_simple, "MSE": mse_simple, "RMSE": rmse_simple, "R2": r2_simple},
    "Multiple_LR": {"MAE": mae_multiple, "MSE": mse_multiple, "RMSE": rmse_multiple, "R2": r2_multiple}
}
results_df = pd.DataFrame(results)
results_df.to_csv("/home/ubuntu/model_evaluation_results.csv")
print("\nEvaluation results saved to /home/ubuntu/model_evaluation_results.csv")


