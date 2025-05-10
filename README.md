# Scrape2Predict: E-Commerce Trends

**Scrape2Predict** is a machine learning-based data analysis project focused on uncovering patterns and predicting outcomes from e-commerce product data. It involves web scraping, data preprocessing, visualizations, and applying ML models to predict product prices based on features like rating and category.

## Project Overview

- **Web Scraping**: Collected real-time product data from an e-commerce website using `requests` and `BeautifulSoup`.
- **Data Cleaning & Imputation**: Handled missing values using `SimpleImputer`.
- **Feature Engineering**: Extracted useful attributes such as `Rating`, `Price`, and `Category`.
- **ML Model**: Trained a Linear Regression model to predict prices based on product ratings.
- **Visualization**: Created scatter plots and regression lines to interpret model performance.
- **Evaluation**: Calculated model accuracy and fine-tuned parameters using GridSearchCV.

---

## Problem Statement

To analyze and predict product price trends using scraped e-commerce data and machine learning, helping users understand how ratings and features influence pricing.

## Solution

We used web scraping for data collection, applied cleaning techniques, trained a regression model, and visualized the results. This provides insights into price prediction and product performance.


## Model Result and Visualization

### Accuracy Plot 
![Accuracy Plot](assets/images/accuracy_plot.png)

### HyperParameter Tuning Results
![Hyperparameter Tuning](assets/images/feature_importance_hyperparameter_tuning.png)
