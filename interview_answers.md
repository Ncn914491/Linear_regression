# Linear Regression Interview Questions and Answers

Here are the answers to the provided interview questions regarding linear regression:

**1. What assumptions does linear regression make?**

Linear regression relies on several key assumptions for the model to be valid and the results interpretable. These are often remembered by the acronym LINE:

*   **Linearity:** The relationship between the independent variables (features) and the dependent variable (target) is assumed to be linear. This means the change in the dependent variable for a one-unit change in an independent variable is constant.
*   **Independence:** The observations (or errors/residuals) are assumed to be independent of each other. This means that the residual for one observation does not predict the residual for another. This is particularly important for time-series data where autocorrelation can be an issue.
*   **Normality:** The errors (residuals) are assumed to be normally distributed, especially for smaller sample sizes. This assumption is important for hypothesis testing and constructing confidence intervals for the coefficients.
*   **Equal Variance (Homoscedasticity):** The errors (residuals) are assumed to have constant variance across all levels of the independent variables. This means the spread of the residuals should be roughly the same as you move along the predicted values line. Violation of this is called heteroscedasticity.
*   **No Multicollinearity (for Multiple Regression):** The independent variables should not be highly correlated with each other. High multicollinearity makes it difficult to determine the individual effect of each independent variable on the dependent variable, leading to unstable coefficient estimates.

**2. How do you interpret the coefficients?**

The interpretation depends on whether it's a simple or multiple linear regression:

*   **Intercept (β₀):** This is the predicted value of the dependent variable when all independent variables are equal to zero. Often, this value doesn't have a practical real-world interpretation, especially if having zero values for all predictors is impossible or outside the range of the observed data (as seen in our house price model interpretation).
*   **Slope Coefficient (βᵢ for feature xᵢ):**
    *   **In Simple Linear Regression:** The coefficient represents the change in the dependent variable for a one-unit increase in the independent variable. For example, in our simple model, the `sqft_living` coefficient of ~279.55 means that for each additional square foot of living area, the predicted house price increases by about $279.55.
    *   **In Multiple Linear Regression:** The coefficient represents the change in the dependent variable for a one-unit increase in *that specific* independent variable, **holding all other independent variables in the model constant**. For example, the `bathrooms` coefficient of ~46402.20 means that for each additional bathroom, the predicted price increases by about $46,402.20, assuming all other features (like sqft_living, bedrooms, grade, etc.) remain unchanged.

**3. What is R² score and its significance?**

*   **Definition:** R-squared (R²), also known as the coefficient of determination, is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s) included in the model.
*   **Range:** It ranges from 0 to 1 (or 0% to 100%).
*   **Significance:**
    *   An R² of 0 indicates that the model explains none of the variability of the response data around its mean.
    *   An R² of 1 indicates that the model explains all the variability of the response data around its mean.
    *   In general, a higher R² indicates that the model fits the data better. For our models, the simple regression had an R² of 0.4941, meaning it explained about 49.4% of the variance in house prices using only `sqft_living`. The multiple regression had an R² of 0.6956, explaining about 69.6% of the price variance using all included features, indicating a better fit.
*   **Caution:** R² alone doesn't determine if a model is good. A high R² can occur even if the model violates assumptions. Also, R² tends to increase as more predictors are added, even if they aren't truly useful. Adjusted R², which penalizes the addition of non-significant predictors, is often preferred in multiple regression.

**4. When would you prefer MSE over MAE?**

Both Mean Squared Error (MSE) and Mean Absolute Error (MAE) are common metrics for evaluating regression models.

*   **MAE (Mean Absolute Error):** Calculates the average of the absolute differences between predicted and actual values. `MAE = mean(|y_true - y_pred|)`.
    *   It's less sensitive to outliers because it doesn't square the errors.
    *   The resulting value is in the same units as the target variable, making it more interpretable.
*   **MSE (Mean Squared Error):** Calculates the average of the squared differences between predicted and actual values. `MSE = mean((y_true - y_pred)²)`.
    *   It penalizes larger errors more heavily due to the squaring term. This makes it more sensitive to outliers.
    *   The units are the square of the target variable's units, making it less directly interpretable (often RMSE, the square root of MSE, is used for interpretability).

*   **Preference:**
    *   **Prefer MSE (or RMSE)** when large errors are particularly undesirable and should be penalized more severely. If outliers are important and need to be highlighted, MSE will reflect their impact more strongly.
    *   **Prefer MAE** when you want a metric that is more robust to outliers or when you want the error metric to be in the same units as the target variable for easier interpretation. If outliers exist but are considered anomalies that shouldn't dominate the error metric, MAE might be better.

**5. How do you detect multicollinearity?**

Multicollinearity occurs in multiple regression when independent variables are highly correlated with each other. It doesn't necessarily reduce the predictive power of the model as a whole, but it makes the interpretation of individual coefficients unreliable.

Methods to detect multicollinearity include:

*   **Correlation Matrix:** Calculate the pairwise correlation between all independent variables. High correlation coefficients (e.g., > 0.7 or 0.8, though the threshold is subjective) between pairs of predictors suggest potential multicollinearity.
*   **Variance Inflation Factor (VIF):** This is the most common method. VIF measures how much the variance of an estimated regression coefficient is increased because of multicollinearity.
    *   Calculate VIF for each independent variable.
    *   `VIF = 1 / (1 - R²_i)`, where R²_i is the R-squared value obtained by regressing the i-th predictor on all other predictors.
    *   **Interpretation:**
        *   VIF = 1: No correlation.
        *   1 < VIF < 5: Moderate correlation, often acceptable.
        *   VIF > 5 or 10: High correlation, indicating significant multicollinearity that likely needs addressing.
*   **Eigenvalues:** Analyzing the eigenvalues of the correlation matrix of predictors can also reveal multicollinearity.
*   **Coefficient Instability:** Observe if coefficients change drastically when adding or removing related predictors or when using different subsets of the data.

**6. What is the difference between simple and multiple regression?**

*   **Simple Linear Regression:**
    *   Involves **one** independent variable (predictor) and one dependent variable (target).
    *   The goal is to model the linear relationship between these two variables.
    *   Equation: `Y = β₀ + β₁X + ε`
    *   Example: Predicting house price (`Y`) based solely on square footage (`X`).
*   **Multiple Linear Regression:**
    *   Involves **two or more** independent variables (predictors) and one dependent variable (target).
    *   The goal is to model the linear relationship between the dependent variable and *multiple* independent variables simultaneously.
    *   Equation: `Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε`
    *   Example: Predicting house price (`Y`) based on square footage (`X₁`), number of bedrooms (`X₂`), location (e.g., latitude `X₃`, longitude `X₄`), grade (`X₅`), etc.
    *   Allows for controlling the effects of multiple factors to understand the unique contribution of each predictor (assuming low multicollinearity).

**7. Can linear regression be used for classification?**

While linear regression is designed for predicting continuous outcomes, it's generally **not suitable** for classification tasks (predicting discrete categories).

*   **Why not?**
    *   **Output Range:** Linear regression outputs continuous values, potentially outside the range of valid probabilities (e.g., < 0 or > 1 if trying to predict probability).
    *   **Thresholding Issues:** If you try to use a threshold (e.g., predict class 1 if output > 0.5, else class 0), the linear nature doesn't fit the typical S-shaped probability curve needed for classification. The decision boundary it creates is sensitive to outliers.
    *   **Assumption Violation:** Classification problems often violate the linear regression assumptions, particularly normality and homoscedasticity of errors.
*   **Alternatives:** Algorithms specifically designed for classification, such as **Logistic Regression**, Support Vector Machines (SVM), Decision Trees, Random Forests, etc., are much more appropriate. Logistic Regression, despite its name, is a classification algorithm that models the probability of a binary outcome using a sigmoid function, ensuring outputs are between 0 and 1.

**8. What happens if you violate regression assumptions?**

Violating the assumptions of linear regression can lead to various problems:

*   **Linearity Violation:** The model will be misspecified, leading to biased predictions and an inability to capture the true underlying relationship. The R² might be low, and patterns might be visible in residual plots.
*   **Independence Violation (Autocorrelation):** Standard errors of the coefficients will likely be underestimated, leading to overly narrow confidence intervals and potentially incorrect conclusions about the statistical significance of predictors (inflated t-statistics, deflated p-values).
*   **Normality Violation:** Affects the validity of hypothesis tests (t-tests, F-test) and confidence intervals, especially with small sample sizes. However, linear regression is somewhat robust to violations of normality with larger sample sizes due to the Central Limit Theorem.
*   **Homoscedasticity Violation (Heteroscedasticity):** While coefficient estimates remain unbiased, the standard errors become biased (usually underestimated). This again invalidates standard hypothesis tests and confidence intervals. Predictions might be less reliable in areas where variance is high.
*   **Multicollinearity Violation:** Coefficient estimates become unstable and highly sensitive to small changes in the data or model specification. Standard errors inflate, making it hard to assess the individual importance of correlated predictors. The overall predictive power of the model might still be okay, but interpreting individual coefficients becomes problematic.

In summary, violating assumptions can lead to biased coefficients, incorrect standard errors, unreliable hypothesis tests and confidence intervals, and poor predictive performance. It's crucial to check these assumptions (e.g., using residual plots, statistical tests like Breusch-Pagan for homoscedasticity, Durbin-Watson for autocorrelation, VIF for multicollinearity) and take corrective actions if needed (e.g., transforming variables, using robust standard errors, removing predictors, using different modeling techniques).
