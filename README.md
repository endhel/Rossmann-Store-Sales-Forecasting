# Rossmann Store Sales Forecasting

<p align="center">
  <img src="img/rossmann_img.png">
</p>

# 1. Problem

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.

After a meeting between Rossmann's directors, managers and CEO, it was planned that the stores should be renovated. However, in order to raise funds for the renovation, it was necessary to forecast sales more accurately, so the business team decided to **forecast the sales for the next 6 weeks of the stores using machine learning models, in order to know if the budget will be enough for the renovation.**

# 2. Business Assumptions

The following assumptions were made about the business problem:

- For stores that did not have "CompetitionDistance" information, it was assumed that the distance would be 2 times greater than the greatest distance from the nearest competitor.
- As it was assumed that there is a competitor even if very far away, if there is no date on which the competitor opened or data regarding promotional periods, we work with the date of the store considering the premise that some variables derived from time are extremely important for represent a behavior.
- Customers data was discarded. Maybe it could be scope for another complementary project to this one.
- The days when the stores were closed were not used.
- Entries whose sales were equal to 0 were not used.

# 3. Solution Proposal

- Granularity (hour, day, year, etc) => 6 weeks
- Problem Type (Classification, Regression, Clustering, etc) => Regression
- Delivery format (dashboard, web page, csv, etc) => Web page

## 3.1. Solution Strategy

The strategy to solve this challenge was:

**Step 01. Data Description:** Use statistics metrics to indentify data outside the scope of the business.

**Step 02. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.

**Step 03. Data Filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.

**Step 04. Exploratory Data Analysis:** Explore data to find insights and better understand the impact of variables on model learning.

**Step 05. Data Preparation:** Prepare the data so that the Machine Learning models can learn the specific behavior.

**Step 06. Feature Selection:** Selection of the most significant attributes for training the models.

**Step 07. Machine Learning Modelling:** Machine Learning model training.

**Step 08. Hyperparameter Fine Tuning:** Choose the best values for each of the parameters of the model selected from the previous step.

**Step 09. Convert Model Performance to Business Values:** Convert the performance of the Machine Learning models into a business result.

**Step 10. Deploy Model to Production:** Publish the model in a cloud environment so that other people or services can use the results to improve the business decision.

**To access the Web page, click below:**

[<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>](https://rossmann-sales-forecasting.herokuapp.com)

# 4. Top 4 Data Insights

**Hypothesis 8.** Stores should sell more over the years.

**FALSE** Stores sell less over the years.

**Hypothesis 9.** Stores should sell more in the second half of the year.

**FALSE** Stores sell less in the second half of the year.

**Hypothesis 10.** Stores should sell more after the 10th of each month.

**TRUE** Stores sell more after the 10th of each month.

**Hypothesis 11.** Stores should sell less on weekends.

**TRUE** Stores sell less on weekends.

# 5. Machine Learning Models Aplied

The tests were performed using the following algorithms:

**Average Model**

**Linear Regression Model**

**Linear Regression Regularized Model - Lasso**

**Random Forest Regressor**

**XGBoost Regressor**

# 6. Machine Learning Model Performance

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

# 7. Conversion of model performance into business values

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


# 8. Conclusion

At the end of this project it was possible to understand how the performance of machine learning models can be converted to business values, especially for regression problems. In addition, it was gratifying to see the final result, with the model put into production, and being able to be used by any user. The best lesson was to see that the real job of data scientists is not to build models and dashboards, but to generate value for companies through the data and tools they have at their disposal.

# 9. Next Steps 

In order to improve the results of this work, it will be necessary to create new variables that have a greater influence on the sales phenomenon. Furthermore, a more robust method can be used to find the best hyperparameters for the model, and use different techniques to handle missing values and to rescale the data.



