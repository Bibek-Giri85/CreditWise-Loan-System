import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="CreditWise Loan System",
    page_icon="🏦",
    layout="wide"
)


# =====================================================
# LOAD MODEL AND PREPROCESSORS
# =====================================================

model = joblib.load("model.pkl")

scaler = joblib.load("scaler.pkl")

ohe = joblib.load("encoder.pkl")

education_encoder = joblib.load(
    "education_encoder.pkl"
)

num_imputer = joblib.load(
    "num_imputer.pkl"
)

cat_imputer = joblib.load(
    "cat_imputer.pkl"
)


# =====================================================
# TITLE
# =====================================================

st.title("🏦 CreditWise Loan System")

st.write(
    "Enter applicant information to predict "
    "whether the loan is likely to be approved."
)


st.divider()


# =====================================================
# APPLICANT INFORMATION
# =====================================================

st.header("👤 Applicant Information")


col1, col2, col3 = st.columns(3)


with col1:

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0.0,
        value=10000.0,
        step=500.0
    )

    age = st.number_input(
        "Age",
        min_value=21,
        max_value=59,
        value=40
    )

    dependents = st.number_input(
        "Dependents",
        min_value=0,
        max_value=3,
        value=1
    )

    gender = st.selectbox(
        "Gender",
        [
            "Female",
            "Male"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Married",
            "Single"
        ]
    )


with col2:

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=550.0,
        max_value=799.0,
        value=678.0
    )

    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        max_value=4,
        value=2
    )

    employment_status = st.selectbox(
        "Employment Status",
        [
            "Contract",
            "Salaried",
            "Self-employed",
            "Unemployed"
        ]
    )

    education_level = st.selectbox(
        "Education Level",
        [
            "Graduate",
            "Not Graduate"
        ]
    )


with col3:

    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.10,
        max_value=0.60,
        value=0.34,
        step=0.01
    )

    savings = st.number_input(
        "Savings",
        min_value=0.0,
        value=10000.0,
        step=500.0
    )

    collateral_value = st.number_input(
        "Collateral Value",
        min_value=0.0,
        value=25000.0,
        step=500.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=20000.0,
        step=500.0
    )

    loan_term = st.number_input(
        "Loan Term",
        min_value=12,
        max_value=84,
        value=48,
        step=12
    )


# =====================================================
# LOAN INFORMATION
# =====================================================

st.header("💰 Loan Information")


col4, col5, col6 = st.columns(3)


with col4:

    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Business",
            "Car",
            "Education",
            "Home",
            "Personal"
        ]
    )


with col5:

    property_area = st.selectbox(
        "Property Area",
        [
            "Rural",
            "Semiurban",
            "Urban"
        ]
    )


with col6:

    employer_category = st.selectbox(
        "Employer Category",
        [
            "Government",
            "MNC",
            "Private",
            "Unemployed"
        ]
    )


st.divider()


# =====================================================
# PREDICTION
# =====================================================

if st.button(
    "🔍 Predict Loan Approval",
    type="primary",
    use_container_width=True
):

    # -------------------------------------------------
    # CREATE INPUT DATAFRAME
    # -------------------------------------------------

    input_df = pd.DataFrame({

        "Applicant_Income": [
            applicant_income
        ],

        "Coapplicant_Income": [
            coapplicant_income
        ],

        "Employment_Status": [
            employment_status
        ],

        "Age": [
            age
        ],

        "Marital_Status": [
            marital_status
        ],

        "Dependents": [
            dependents
        ],

        "Credit_Score": [
            credit_score
        ],

        "Existing_Loans": [
            existing_loans
        ],

        "DTI_Ratio": [
            dti_ratio
        ],

        "Savings": [
            savings
        ],

        "Collateral_Value": [
            collateral_value
        ],

        "Loan_Amount": [
            loan_amount
        ],

        "Loan_Term": [
            loan_term
        ],

        "Loan_Purpose": [
            loan_purpose
        ],

        "Property_Area": [
            property_area
        ],

        "Education_Level": [
            education_level
        ],

        "Gender": [
            gender
        ],

        "Employer_Category": [
            employer_category
        ]
    })


    # -------------------------------------------------
    # EDUCATION ENCODING
    # -------------------------------------------------

    input_df["Education_Level"] = (
        education_encoder.transform(
            input_df["Education_Level"]
        )
    )


    # -------------------------------------------------
    # ONE-HOT ENCODING
    # -------------------------------------------------

    cols = [
        "Employment_Status",
        "Marital_Status",
        "Loan_Purpose",
        "Property_Area",
        "Gender",
        "Employer_Category"
    ]


    encoded = ohe.transform(
        input_df[cols]
    )


    encoded_df = pd.DataFrame(
        encoded,
        columns=ohe.get_feature_names_out(cols)
    )


    input_df = pd.concat(
        [
            input_df.drop(
                columns=cols
            ).reset_index(drop=True),

            encoded_df.reset_index(drop=True)
        ],
        axis=1
    )


    # -------------------------------------------------
    # FEATURE ENGINEERING
    # -------------------------------------------------

    input_df["DTI_Ratio_sq"] = (
        input_df["DTI_Ratio"] ** 2
    )

    input_df["Credit_Score_sq"] = (
        input_df["Credit_Score"] ** 2
    )


    # -------------------------------------------------
    # SCALE
    # -------------------------------------------------

    input_scaled = scaler.transform(
        input_df
    )


    # -------------------------------------------------
    # PREDICTION
    # -------------------------------------------------

    prediction = model.predict(
        input_scaled
    )[0]


    probabilities = model.predict_proba(
        input_scaled
    )[0]


    # -------------------------------------------------
    # DISPLAY
    # -------------------------------------------------

    st.subheader("📊 Prediction Result")


    if prediction == 1:

        st.success(
            "🎉 Loan Approved"
        )

        approval_probability = (
            probabilities[1] * 100
        )

        st.metric(
            "Approval Probability",
            f"{approval_probability:.2f}%"
        )

    else:

        st.error(
            "❌ Loan Not Approved"
        )

        rejection_probability = (
            probabilities[0] * 100
        )

        st.metric(
            "Non-Approval Probability",
            f"{rejection_probability:.2f}%"
        )


    # -------------------------------------------------
    # SHOW INPUT
    # -------------------------------------------------

    with st.expander(
        "View Applicant Information"
    ):

        st.dataframe(
            input_df,
            use_container_width=True
        )