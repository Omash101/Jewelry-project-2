# Jewelry-project-2
# Gemineye Pricing Optimization Analysis
![image](https://github.com/user-attachments/assets/bf3a5711-0619-4138-a7e1-c7957630c182)


##  Project Overview
This repository contains an in-depth analysis of **pricing optimization for Gemineye**, a luxury jewelry retailer. The goal of this project is to **improve pricing efficiency** by addressing:
- Overpricing that may drive away price-sensitive customers.
- Underpricing that reduces profit margins.
- Difficulty in dynamic price adjustments based on market trends, customer preferences, and competition.

##  Problem Statement
Gemineye currently uses **manual pricing adjustments**, leading to inefficiencies such as:
- Inconsistent pricing strategies across regions and product lines.
- Lack of a data-driven approach to demand elasticity.
- Slow responses to competitive market changes.

##  Objectives
- Implement a **data-driven pricing strategy** using demand elasticity models.
- Improve real-time price optimization based on market trends.
- Reduce manual effort and increase accuracy in pricing decisions.

##  Methodology
1. Business Understanding  
2. Data Understanding  
3. Data preparation
4. Exploratory Data Analysis (EDA)
5. Data modelling ( Carry out feature engineering)
6. Model Evaluation 
7. Segmentation analysis
8. Experiment Tracking with MLFLOW
9. Model Deployment
10. Insight and Recommendation

## Data Source
The dataset used in this project was provided by Amdari. The data contains a collection of features like purchased product id, price in USD and other relevant information.

## Data Preprocessing
Before feeding the data into the machine learning model, extensive data preprocessing was done. This include handling missing values, scaling features, and addressing class imbalance.

## Data modeling (Machine learning
The model is built using a supervised machine learning approach.Training and Test data was split. Several Regression algorithms were experimented with including but not limited to:
- **Linear Regression**
- **CatBoostRegressor**
- **AdaBoostRegressor**
- **XGBoostRegressor**
- **LightgbmRegresor**
- **DecisionTreeRegressor**
The Regression algorithms was preferred over the Classifier algorithms because is used when predicting continuous values (e.g., stock prices, temperature).

## Model Evaluation
To assess the performance of the machine learning model, the following evaluation metrics were used.
- **R2:** It evaluates how well a regression model fits the data. It indicates the proportion of the variance in the dependent variable that is explained by the independent variables.

- **RMSE:** used metric for evaluating the accuracy of a regression model. It measures how far the predicted values are from the actual values.

## Segmentation Analysis
Because the Regression model's prediction are constantly low or inaccurate, meaning the model is not capturing important variations in the data. The use of Segmentation analysis helps to improve predictive accuracy by identifying subgroups within the datasets that behave differently.

## Key Insight
- CatBoostRegressor is the best model as it supports categorical features and works well with missing data
- CatBoostRegressor perfromed better than the other models based of its RMSE score.The performance is quite low meaning there is still large errors
- The predicted values of all the models are significantly deviating from the actual values. Meaning the models are making large errors leading to poor prediction.
- By segmenting the data into meaningful groups, you can train separate models for each segment, reducing prediction errors.

## Segmentation insight
## Cluster 0:
- Price-sensitive customers: Offer discounts and bundled deals.
- Occasional buyers: Engage with email marketing and seasonal promotions.
- Total Orders: 71269 - Adjust inventory and stock availability accordingly.
  
## Cluster 1:
- High-spending customers: Consider premium offers and personalized promotions.
- Occasional buyers: Engage with email marketing and seasonal promotions.
- Total Orders: 1466 - Adjust inventory and stock availability accordingly.

## Cluster 2:
- High-spending customers: Consider premium offers and personalized promotions.
- Occasional buyers: Engage with email marketing and seasonal promotions.
- Total Orders: 6 - Adjust inventory and stock availability accordingly.

## Cluster 3:
- Price-sensitive customers: Offer discounts and bundled deals.
- Occasional buyers: Engage with email marketing and seasonal promotions.
- Total Orders: 17817 - Adjust inventory and stock availability accordingly.




