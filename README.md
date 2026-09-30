# 💎 Diamond Price Prediction using Snowflake

## Business Intelligence Assignment

This project was completed as part of a Business Intelligence assignment to gain hands-on experience with Snowflake, Machine Learning, Python, Snowpark, and Streamlit.

## Project Overview

The objective of this project is to predict diamond prices using machine learning regression models.

The project demonstrates an end-to-end workflow including:

- Creating a Snowflake database and schema
- Loading a real-world dataset into Snowflake
- Data preparation and train/test splitting
- Machine learning model training
- Model evaluation and comparison
- Building an interactive Streamlit application
- Deploying the application using Snowflake

## Dataset

**Dataset:** Diamonds Dataset  
**Source:** Kaggle  
**Number of records:** 53,940

Dataset URL:

https://www.kaggle.com/shivam2503/diamonds

The dataset contains diamond characteristics such as carat, cut, color, clarity, depth, table, dimensions, and price.

## Snowflake Environment

**Database:** DIAMOND_PRICE_ML

**Schema:** ML_WORKFLOW

**Raw Table:** DIAMONDS_RAW

## Machine Learning Models

Two regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor

## Model Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 735.41 | 1131.67 | 0.9195 |
| Random Forest Regressor | 276.79 | 560.30 | 0.9803 |

The Random Forest Regressor produced the recorded test R² of 0.9803.

## Streamlit Application

The project includes an interactive Streamlit application that:

- Displays the dataset overview
- Shows model performance
- Allows users to explore diamond characteristics
- Provides an estimated price based on similar diamonds
- Displays sample diamond data

## What I Learned

Through this assignment, I gained practical experience using Snowflake as a platform for data and analytics workflows.

I learned how to:

- Create and manage Snowflake databases, schemas, tables, and warehouses
- Load datasets into Snowflake
- Work with data using Python and Snowpark
- Train and evaluate machine learning models
- Compare regression model performance
- Build an interactive Streamlit application
- Deploy a data/ML application through Snowflake

## Technologies Used

- Snowflake
- Snowpark
- Python
- Pandas
- Scikit-learn
- Streamlit
- Machine Learning
- Kaggle

## Project Structure
diamond-price-prediction-snowflake
|
├── README.md                  
├── DIAMOND_PRICE_MODEL_TRAINING.ipynb
├── streamlit_app.py
└── setup.sql
