import pandas as pd
import joblib


# ==========================
# Load Model
# ==========================

model = joblib.load(
    "models/churn_prediction_model.pkl"
)

print(
    "Model Loaded Successfully"
)


# ==========================
# Get EXACT training columns
# ==========================

feature_names = model.feature_names_in_

print(
    "\nNumber of features:",
    len(feature_names)
)


# ==========================
# Create Empty Customer
# ==========================

sample_customer = pd.DataFrame(
    [[0]*len(feature_names)],
    columns=feature_names
)



# ==========================
# Customer Information
# ==========================


sample_customer.loc[
    0,
    "tenure"
] = 2


sample_customer.loc[
    0,
    "MonthlyCharges"
] = 90


sample_customer.loc[
    0,
    "TotalCharges"
] = 180



# Set categorical values ONLY if model knows them


values = [

    "Contract_Month-to-month",

    "PaymentMethod_Electronic check",

    "InternetService_Fiber optic"

]


for col in values:

    if col in feature_names:

        sample_customer.loc[
            0,
            col
        ] = 1



# ==========================
# Predict
# ==========================


prediction = model.predict(
    sample_customer
)


probability = model.predict_proba(
    sample_customer
)[0][1]



print(
    "\n---------------------"
)



if prediction[0] == 1:

    print(
        "High Risk Customer - Likely to Churn"
    )


else:

    print(
        "Low Risk Customer - Likely to Stay"
    )



print(

    "Churn Probability:",
    round(
        probability*100,
        2
    ),
    "%"

)