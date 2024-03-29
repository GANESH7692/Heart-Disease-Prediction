# -*- coding: utf-8 -*-
"""Heart-Disease-Prediction-Using-Machine-Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sSTIasBLruFSgZVkkL5m-prRIQbgqe5O
"""

# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Loading the dataset
data = pd.read_csv('/content/heart.csv')

# Exploratory Data Analysis
print(data.head())  # Display the first 5 rows of the dataset
print(data.shape)    # Check the shape of the dataset(displays the no.of rows and columns)

print(data['target'].value_counts())
# 0 represents a healthy heart, 1 represents a heart disease

# Split features and target variable
X = data.drop(columns='target', axis=1)  # Features
y = data['target']  # Target variable

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Model Training
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Model Evaluation
y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print('Training Accuracy: {:.2f}%'.format(train_accuracy * 100))

y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print('Testing Accuracy: {:.2f}%'.format(test_accuracy * 100))

# More detailed evaluation metrics
print('Classification Report:')
print(classification_report(y_test, y_test_pred))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_test_pred))

# Building a Prediction System with Risk Score
def predict_heart_disease_risk(model, data):
    prob_prediction = model.predict_proba(data)
    return prob_prediction[0][1]  # Probability of having heart disease (class 1)

def provide_health_advice(risk_score):
    if risk_score <= 20:
        return "Your risk is low. Keep up the good work with healthy habits!"
    elif risk_score <= 50:
        return "You're at a moderate risk. Consider a balanced diet and regular exercise."
    elif risk_score <= 80:
        return "Your risk is relatively high. Consult a healthcare professional and focus on healthier choices."
    else:
        return "Your risk is very high. Seek immediate medical advice and adopt a healthier lifestyle."

# Mapping column names to patient details
patient_details_1 = {
    'age': 62, 'sex': 0, 'cp': 0, 'trestbps': 140, 'chol': 268,
    'fbs': 0, 'restecg': 0, 'thalach': 160, 'exang': 0, 'oldpeak': 3.6,
    'slope': 0, 'ca': 2, 'thal': 2, 'target': 'Not specified'
}

patient_details_2 = {
    'age': 56, 'sex': 1, 'cp': 1, 'trestbps': 120, 'chol': 236,
    'fbs': 0, 'restecg': 1, 'thalach': 178, 'exang': 0, 'oldpeak': 0.8,
    'slope': 2, 'ca': 0, 'thal': 2, 'target': 'Not specified'
}

# Displaying patient details
print("\nPatient 1 Details:")
for key, value in patient_details_1.items():
    print(f"{key.capitalize()}: {value}")

print("\nPatient 2 Details:")
for key, value in patient_details_2.items():
    print(f"{key.capitalize()}: {value}")

# Example predictions with risk scores
input_data_1 = np.array(list(patient_details_1.values())[:-1]).reshape(1, -1)
input_data_2 = np.array(list(patient_details_2.values())[:-1]).reshape(1, -1)

# Example predictions with risk scores
risk_score_1 = predict_heart_disease_risk(model, input_data_1)
risk_score_2 = predict_heart_disease_risk(model, input_data_2)

# Providing health advice based on risk scores
advice_patient_1 = provide_health_advice(risk_score_1 * 100)
advice_patient_2 = provide_health_advice(risk_score_2 * 100)

# Displaying health advice and risk scores for patients
print('\nRisk Score for Patient 1: {:.2f}%'.format(risk_score_1 * 100))
print('Health Advice for Patient 1:', advice_patient_1)

print('\nRisk Score for Patient 2: {:.2f}%'.format(risk_score_2 * 100))
print('Health Advice for Patient 2:', advice_patient_2)