import pandas as pd
import joblib
import matplotlib
matplotlib.use("Agg") # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# Load the test data
X_test = pd.read_csv("/home/ubuntu/X_test.csv")
y_test = pd.read_csv("/home/ubuntu/y_test.csv")["price"] # Ensure y_test is a Series

# Load the saved models
simple_lr_model = joblib.load("/home/ubuntu/simple_linear_regression_model.joblib")
multiple_lr_model = joblib.load("/home/ubuntu/multiple_linear_regression_model.joblib")

# --- Plot Simple Linear Regression ---
simple_feature = "sqft_living" # Must match the feature used in training
X_test_simple = X_test[[simple_feature]]
y_pred_simple = simple_lr_model.predict(X_test_simple)

print(f"\n--- Plotting Simple Linear Regression (Feature: {simple_feature}) ---")
plt.figure(figsize=(10, 6))
plt.scatter(X_test_simple, y_test, alpha=0.5, label="Actual Prices")
plt.plot(X_test_simple, y_pred_simple, color="red", linewidth=2, label="Regression Line")
plt.title(f"Simple Linear Regression: Price vs. {simple_feature}")
plt.xlabel(simple_feature)
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plot_path = "/home/ubuntu/simple_regression_plot.png"
plt.savefig(plot_path)
print(f"Simple regression plot saved to {plot_path}")
plt.close() # Close the plot to free memory

# --- Interpret Coefficients ---
interpretations = []

# Simple Model Interpretation
interpretations.append("## Simple Linear Regression Model Interpretation")
interpretations.append(f"Feature: `{simple_feature}`")
simple_coeff = simple_lr_model.coef_[0]
simple_intercept = simple_lr_model.intercept_
interpretations.append(f"- **Coefficient (`{simple_feature}`):** {simple_coeff:.2f}")
interpretations.append(f"  - Interpretation: For each additional square foot of living area, the predicted house price increases by approximately ${simple_coeff:.2f}, holding all other factors constant (though none were included in this simple model).")
interpretations.append(f"- **Intercept:** {simple_intercept:.2f}")
interpretations.append(f"  - Interpretation: The intercept represents the predicted price when the `{simple_feature}` is zero. In this context, a house with 0 sqft living area is unrealistic, so the intercept of ${simple_intercept:.2f} doesn't have a practical meaning other than adjusting the line's position.")

# Multiple Model Interpretation
interpretations.append("\n## Multiple Linear Regression Model Interpretation")
multiple_coeffs = pd.Series(multiple_lr_model.coef_, index=X_test.columns)
multiple_intercept = multiple_lr_model.intercept_

interpretations.append("- **Coefficients:**")
for feature, coeff in multiple_coeffs.items():
    interpretations.append(f"  - **`{feature}`:** {coeff:.2f}")
    # Add specific interpretations based on feature meaning
    if feature == "bedrooms":
        interpretations.append(f"    - Interpretation: Holding all other features constant, each additional bedroom is associated with a decrease in predicted price by approximately ${abs(coeff):.2f}. This might seem counter-intuitive and could be due to multicollinearity or other factors in the model.")
    elif feature == "bathrooms":
        interpretations.append(f"    - Interpretation: Holding all other features constant, each additional bathroom is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "sqft_living":
        interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot of living area is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "sqft_lot":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot of lot size is associated with a very small increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "floors":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional floor is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "waterfront":
         interpretations.append(f"    - Interpretation: Holding all other features constant, having a waterfront view (value 1 vs 0) is associated with a significant increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "view":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each unit increase in the view rating is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "condition":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each unit increase in the condition rating is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "grade":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each unit increase in the grade rating is associated with a significant increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "sqft_above":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot above ground is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "sqft_basement":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot of basement area is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "yr_built":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each year newer the house was built is associated with a decrease in predicted price by approximately ${abs(coeff):.2f}. This could be counter-intuitive and might relate to other correlated features like location or renovation status.")
    elif feature == "yr_renovated":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each year more recent the renovation (or if renovated vs not, depending on how 0 is coded) is associated with a small increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "lat":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each unit increase in latitude is associated with a large increase in predicted price by approximately ${coeff:.2f}. Latitude likely captures geographic value differences.")
    elif feature == "long":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each unit increase in longitude (moving east) is associated with a decrease in predicted price by approximately ${abs(coeff):.2f}. Longitude also likely captures geographic value differences.")
    elif feature == "sqft_living15":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot of living area for the nearest 15 neighbors is associated with an increase in predicted price by approximately ${coeff:.2f}.")
    elif feature == "sqft_lot15":
         interpretations.append(f"    - Interpretation: Holding all other features constant, each additional square foot of lot size for the nearest 15 neighbors is associated with a small decrease in predicted price by approximately ${abs(coeff):.2f}.")

interpretations.append(f"\n- **Intercept:** {multiple_intercept:.2f}")
interpretations.append(f"  - Interpretation: The intercept represents the predicted price when all feature values are zero. Similar to the simple model, this value (${multiple_intercept:.2f}) often lacks practical meaning in real-world scenarios where features cannot realistically be zero simultaneously (e.g., 0 sqft, 0 bedrooms, built in year 0 at lat/long 0).")

# Save interpretations to file
interpretation_path = "/home/ubuntu/model_interpretations.md"
with open(interpretation_path, "w") as f:
    f.write("\n".join(interpretations))

print(f"\nModel interpretations saved to {interpretation_path}")


