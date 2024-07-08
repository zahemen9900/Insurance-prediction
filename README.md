
# Insurance Premium Prediction App

Welcome to the Insurance Premium Prediction App! This application allows users to predict monthly insurance premiums based on various features such as gender, occupation, policy duration, and plan type.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Data Preprocessing](#data-preprocessing)
- [Model](#model)
- [How to Use](#how-to-use)
- [Access the App](#access-the-app)

## Introduction
The Insurance Premium Prediction App is designed to predict the monthly premium amount for insurance policies. By leveraging machine learning algorithms, this app provides accurate predictions based on input features provided by the user.

## Features
- **User Input**: Enter details such as gender, occupation, policy duration, and plan type.
- **Prediction**: Get an instant prediction of the monthly premium based on the provided inputs.
- **Model**: The app uses a Random Forest Regressor for prediction, tuned for optimal performance.

## Data Preprocessing
The data used for training the model undergoes several preprocessing steps:
- **Scaling**: Numerical features are scaled using MinMaxScaler.
- **Encoding**: Categorical features are encoded using OrdinalEncoder, with handling for unknown values.

## Model
The model used in this application is a `Random Forest Regressor`. The hyperparameters of the model are tuned using `GridSearchCV` to ensure the best performance.

## How to Use
1. **Input Data**: Provide your details such as gender, occupation, policy duration, and plan type.
2. **Predict**: Click on the predict button to get the monthly premium prediction.

## Access the App
You can access the Insurance Premium Prediction App at the following URL:
[Insurance Premium Prediction App](https://insurance-prediction-app-z.streamlit.app/)

