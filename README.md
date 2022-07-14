# Rossmann Store Sales Forecasting

<p align="center">
  <img src="img/rossmann_img.png">
</p>

# 1. Problem

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.

After a meeting between Rossmann's directors, managers and CEO, it was planned that the stores should be renovated. However, in order to raise funds for the renovation, it was necessary to forecast sales more accurately, so the business team decided to **forecast the sales for the next 6 weeks of the stores using machine learning models, in order to know if the budget will be enough for the renovation.**

# 2. Solution Proposal

- Granularity (hour, day, year, etc) => 6 weeks
- Problem Type (Classification, Regression, Clustering, etc) => Regression
- Delivery format (dashboard, web page, csv, etc) => Web page

## 2.1. Solution Strategy

**Step 01:** Data Description

**Step 02:** Feature Engineering

**Step 03:** Data Filtering

**Step 04:** Exploratory Data Analysis

**Step 05:** Data Preparation

**Step 06:** Feature Selection

**Step 07:** Machine Learning Modelling

**Step 08:** Hyperparameter Fine Tuning

**Step 09:** Error Interpretation

**Step 10:** Deploy Model to Production

**To access the Web page, click below:**

[<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>](https://rossmann-sales-forecasting.herokuapp.com)

# 3. Top 4 Data Insights

**Hypothesis 8.** Stores should sell more over the years.

**FALSE** Stores sell less over the years.

**Hypothesis 9.** Stores should sell more in the second half of the year.

**FALSE** Stores sell less in the second half of the year.

**Hypothesis 10.** Stores should sell more after the 10th of each month.

**TRUE** Stores sell more after the 10th of each month.

**Hypothesis 11.** Stores should sell less on weekends.

**TRUE** Stores sell less on weekends.

# 4. Machine Learning Models Aplied

The tests were performed using the following algorithms:

**Average Model**

**Linear Regression Model**

**Linear Regression Regularized Model - Lasso**

**Random Forest Regressor**

**XGBoost Regressor**

# 5. Machine Learning Model Performance

**Single Performance**

| Model Name | MAE | MAPE | RMSE |
|-----------|---------|-----------|---------|
|  Random Forest Regressor |	679.598831 |	0.099913 |	1011.119437
|  Average Model |	1354.800353 |	0.206400 |	1835.135542
|  Linear Regression |	1867.089774 |	0.292694 | 2671.049215
|  Linear Regression - Lasso |	1891.704881 |	0.289106 | 2744.451737 
|  XGBoost Regressor |	6683.423528 |	0.949439 |	7330.693347 

**Real Performance - Cross Validation**

| Model Name | MAE | MAPE | RMSE |
|-----------|---------|-----------|---------|
|  Random Forest Regressor |	836.61 +/- 217.1 |	0.12 +/- 0.02 |	1254.3 +/- 316.17
|  Linear Regression |	2081.73 +/- 295.63 |	0.3 +/- 0.02 |	2952.52 +/- 468.37
|  Linear Regression - Lasso |	2116.38 +/- 341.5 |	0.29 +/- 0.01 |	3057.75 +/- 504.26 
|  XGBoost Regressor |	7049.2 +/- 588.65 |	0.95 +/- 0.0 |	7715.2 +/- 689.51 

The Random Forest model obtained the best results and was chosen to move on to the Hypeparameter Fine Tuning stage.

**Final Performance - Hyperparameter Fine Tunning**

After finding the best parameters for the model using the Random Search method, the final metrics for the model were as follows:

| Model Name | MAE | MAPE | RMSE |
|-----------|---------|-----------|---------|
|  Random Forest Regressor |	673.88146 |	0.098973 |	1003.765266

# 6. Conversion of model performance into business values

**Current model based on average sales**

| Scenario | Values |
|---------|---------|
| Predictions | R$280,754,389.45 |

**Model with Random Forest Regressor**

| Scenario | Values |
|---------|---------|
| Predictions | R$288,623,718.62 |
| Worst Scenario | R$287,868,662.51 |
| Best Scenario | R$289,378,774.72 |

**Difference Between Models**

| Scenario | Values |
|---------|---------|
| Worst Scenario | R$7,114,273.06 |
| Best Scenario | R$8,624,385.27 |


# 7. Conclusion

At the end of this project it was possible to understand how the performance of machine learning models can be converted to business values, especially for regression problems. In addition, it was gratifying to see the final result, with the model put into production, and being able to be used by any user. The best lesson was to see that the real job of data scientists is not to build models and dashboards, but to generate value for companies through the data and tools they have at their disposal.

# 8. Next Steps

In order to improve the results of this work, it will be necessary to create new variables that have a greater influence on the sales phenomenon. Furthermore, a more robust method can be used to find the best hyperparameters for the model, and use different techniques to handle missing values and to rescale the data.



