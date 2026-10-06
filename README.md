# Medical Insurance Cost Prediction
<img width="882" height="747" alt="image" src="https://github.com/user-attachments/assets/a31b3bb6-2cc6-402e-acf5-ee037df2b49c" />

A Machine Learning web application that predicts medical insurance charges based on patient information.

## Project Overview

This project uses multiple regression and tree-based machine learning models to predict medical insurance costs.

The models compared are:

- Multiple Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regression
- Random Forest Regression

The best-performing model is selected based on regression performance metrics such as R² and RMSE.

## Features

- Predict medical insurance charges
- User-friendly Streamlit interface
- Machine Learning based prediction
- Multiple regression models evaluated
- Model performance comparison
- Random Forest based prediction
- Interactive web application

## Input Features

The application uses patient information such as:

- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning

## Project Structure

```text
medical-insurance-cost-prediction/
│
├── app.py
├── best_medical_insurance_model.pkl
├── requirements.txt
└── README.md
```

## How to Run Locally

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

This application can be deployed using Streamlit Community Cloud directly from GitHub.

## Author

Aditi Paul

B.Tech Computer Science Engineering
