# Predicting Customer Churn for a Subscription Streaming Service

## Machine Learning Capstone Project

A complete end-to-end Machine Learning project that predicts whether a customer of a subscription-based streaming service is likely to cancel their subscription (customer churn).

The project applies data analysis, feature selection, model comparison, cross-validation, and hyperparameter optimization to build a reliable churn prediction system.

---

# Problem Statement

Subscription-based businesses such as streaming platforms depend heavily on customer retention.

Customer churn occurs when users cancel their subscriptions. Losing existing customers impacts:

- Revenue growth
- Customer Lifetime Value (CLV)
- Business stability

The objective of this project is to build a Machine Learning model that can identify customers who are likely to churn before cancellation happens.

By predicting high-risk customers early, marketing teams can:

- Provide personalized retention offers
- Improve customer engagement
- Reduce customer loss
- Increase long-term revenue


---

# Business Objective

The Machine Learning system aims to answer:

"Which customers are most likely to cancel their subscription?"

The final model predicts:

- Low Risk Customer → likely to continue subscription
- High Risk Customer → likely to churn


Example Output:

```
Customer Risk: High

Churn Probability: 65.81%
```

---

# Dataset Information

# Dataset Source

Dataset Name:
Telco Customer Churn Dataset

Dataset Provider:
IBM Sample Data Collection

Hosted On:
Kaggle

Dataset Version:
Latest Kaggle version available at project development time

Source URL:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn


File Used:

WA_Fn-UseC_-Telco-Customer-Churn.csv


Dataset Size:

7043 customer records

21 original attributes


Target Variable:

Churn
(Binary Classification)

### Customer Demographics

- Gender
- Senior Citizen status
- Partner
- Dependents


### Subscription Information

- Contract type
- Tenure
- Internet services
- Streaming services


### Billing Information

- Monthly charges
- Total charges
- Payment method


### Target Variable

```
Churn

Yes → Customer cancelled subscription

No → Customer continued subscription
```

---

# Download Dataset

Download the dataset from Kaggle:

https://www.kaggle.com/datasets/blastchar/telco-customer-churn


After downloading, place the CSV file inside:

```
data/
│
└── WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

# Project Structure

```
Customer-Churn-Prediction/

│
├── data/
│   └── dataset.csv
│
├── notebooks/
│
│   ├── 01_EDA.ipynb
│   │
│   ├── 02_Preprocessing_FeatureSelection.ipynb
│   │
│   └── 03_ModelTraining_Evaluation.ipynb
│
├── processed_data/
│   ├── full_features.csv
│   ├── selected_features.csv
│   └── target.csv
│
├── models/
│   └── churn_prediction_model.pkl
│
├── testing.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Machine Learning Workflow

## 1. Exploratory Data Analysis

Performed:

- Dataset overview
- Column analysis
- Missing value detection
- Duplicate checking
- Target variable analysis
- Churn distribution visualization
- Feature relationship analysis
- Correlation analysis


Key insights:

- Month-to-month customers have higher churn
- Contract duration affects retention
- Billing patterns influence cancellation behavior


---

## 2. Data Preprocessing

Steps performed:

### Missing Value Handling

Handled missing values in:

```
TotalCharges
```


### Feature Cleaning

Removed unnecessary columns:

```
customerID
```


### Encoding

Converted categorical features using:

```
One-Hot Encoding
```


### Feature Scaling

Applied:

```
StandardScaler
```


### Data Splitting

Training and testing split:

```
80% Training

20% Testing
```


---

# Feature Selection Techniques

Feature reduction was performed using two methods:


## 1. Correlation Based Feature Selection

Analyzed relationship between features and churn output.

Removed weakly related features.


## 2. Random Forest Feature Importance

Used tree-based importance ranking.

Identified most influential churn factors:

- Contract type
- Tenure
- Monthly charges
- Payment method
- Internet service


---

# Machine Learning Models Implemented

Three classification algorithms were compared:


## Decision Tree Classifier

Tree-based classification model.


## Random Forest Classifier

Ensemble learning model using multiple decision trees.


## Support Vector Machine

Margin-based classification algorithm.


---

# Model Validation

Used:

## K-Fold Cross Validation

Benefits:

- More reliable evaluation
- Reduces dependency on one train-test split
- Tests model stability


---

# Hyperparameter Optimization

Best performing model was tuned using:

```
GridSearchCV
```

Parameters optimized:

```
n_estimators

max_depth

min_samples_split

min_samples_leaf
```


---

# Evaluation Metrics

Models were compared using:

| Metric | Purpose |
|-|-|
|Accuracy|Overall correctness|
|Precision|Correct churn predictions|
|Recall|Finding actual churn customers|
|F1 Score|Precision-recall balance|
|ROC-AUC|Classification performance|


Accuracy alone was not considered enough because churn datasets may have class imbalance.

---

# Visualizations

Included:

- Churn distribution graph
- Feature correlation heatmap
- Feature importance chart
- Confusion matrix
- ROC Curve


---

# Final Model

Selected Model:

```
Random Forest Classifier
```


Reasons:

- Strong prediction performance
- Handles feature interactions well
- Reduces overfitting
- Provides feature importance
- Suitable for business interpretation


---

# Testing The Model

Run:

```
python testing.py
```


Example Result:

```
Model Loaded Successfully


High Risk Customer - Likely to Churn

Churn Probability: 65.81 %
```

---

# Installation and Setup


## 1. Clone Repository


```bash
git clone https://github.com/your-username/Customer-Churn-Prediction.git
```

Move into project:


```bash
cd Customer-Churn-Prediction
```


---

## 2. Create Virtual Environment


Windows:

```bash
python -m venv .venv
```


Activate:

```bash
.venv\Scripts\activate
```


---

## 3. Install Dependencies


```bash
pip install -r requirements.txt
```


---

## 4. Run Jupyter Notebook


```bash
jupyter notebook
```


Execute notebooks in order:


```
1. 01_EDA.ipynb

2. 02_Preprocessing_FeatureSelection.ipynb

3. 03_ModelTraining_Evaluation.ipynb
```


---

# Technologies Used

## Programming Language

- Python


## Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib


## Machine Learning Concepts

- Classification
- Feature Engineering
- Feature Selection
- Cross Validation
- Hyperparameter Tuning
- Model Evaluation


---

# Business Recommendations

Based on model insights:


### Target Low Engagement Customers

Provide personalized offers to inactive users.


### Improve Month-to-Month Retention

Customers with flexible contracts have higher churn risk.


### Personalized Pricing

Offer discounts for customers with high monthly charges.


### Improve Customer Experience

Focus support efforts on customers predicted as high risk.


---

# Future Improvements

Possible enhancements:

- Deploy model using Streamlit
- Create FastAPI prediction API
- Add MLflow experiment tracking
- Docker deployment
- Cloud deployment
- Real-time churn monitoring dashboard


---

# Conclusion

This project demonstrates an end-to-end Machine Learning workflow for solving a real-world customer retention problem.

The system enables subscription businesses to identify potential churn customers early and make data-driven retention decisions.
