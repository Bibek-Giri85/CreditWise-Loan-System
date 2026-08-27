import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("loan_approval_data.csv")

print("Original dataset shape:", df.shape)


# =========================================================
# 2. IDENTIFY COLUMNS
# =========================================================

categorical_cols = df.select_dtypes(
    include=["object"]
).columns

numerical_cols = df.select_dtypes(
    include=["float64"]
).columns


# =========================================================
# 3. HANDLE MISSING NUMERICAL VALUES
# =========================================================

num_imp = SimpleImputer(
    strategy="mean"
)

df[numerical_cols] = num_imp.fit_transform(
    df[numerical_cols]
)


# =========================================================
# 4. HANDLE MISSING CATEGORICAL VALUES
# =========================================================

cat_imp = SimpleImputer(
    strategy="most_frequent"
)

df[categorical_cols] = cat_imp.fit_transform(
    df[categorical_cols]
)


# =========================================================
# 5. REMOVE APPLICANT ID
# =========================================================

df = df.drop(
    "Applicant_ID",
    axis=1
)


# =========================================================
# 6. ENCODE TARGET
# =========================================================

target_encoder = LabelEncoder()

df["Loan_Approved"] = target_encoder.fit_transform(
    df["Loan_Approved"]
)


# =========================================================
# 7. ENCODE EDUCATION LEVEL
# =========================================================

education_encoder = LabelEncoder()

df["Education_Level"] = education_encoder.fit_transform(
    df["Education_Level"]
)


# =========================================================
# 8. ONE-HOT ENCODING
# =========================================================

cols = [
    "Employment_Status",
    "Marital_Status",
    "Loan_Purpose",
    "Property_Area",
    "Gender",
    "Employer_Category"
]


ohe = OneHotEncoder(
    drop="first",
    sparse_output=False,
    handle_unknown="ignore"
)


encoded = ohe.fit_transform(
    df[cols]
)


encoded_df = pd.DataFrame(
    encoded,
    columns=ohe.get_feature_names_out(cols),
    index=df.index
)


df = pd.concat(
    [
        df.drop(columns=cols),
        encoded_df
    ],
    axis=1
)


# =========================================================
# 9. FEATURE ENGINEERING
# =========================================================

df["DTI_Ratio_sq"] = (
    df["DTI_Ratio"] ** 2
)

df["Credit_Score_sq"] = (
    df["Credit_Score"] ** 2
)


# =========================================================
# 10. CREATE X AND Y
# =========================================================

X = df.drop(
    columns=["Loan_Approved"]
)

y = df["Loan_Approved"]


# =========================================================
# 11. TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================================
# 12. FEATURE SCALING
# =========================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# =========================================================
# 13. TRAIN GAUSSIAN NAIVE BAYES
# =========================================================

model = GaussianNB()

model.fit(
    X_train_scaled,
    y_train
)


# =========================================================
# 14. PREDICTION
# =========================================================

y_pred = model.predict(
    X_test_scaled
)


# =========================================================
# 15. EVALUATION
# =========================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)


print("\n====================================")
print("GAUSSIAN NAIVE BAYES RESULTS")
print("====================================")

print(
    f"Accuracy  : {accuracy:.4f}"
)

print(
    f"Precision : {precision:.4f}"
)

print(
    f"Recall    : {recall:.4f}"
)

print(
    f"F1 Score  : {f1:.4f}"
)


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)


print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# =========================================================
# 16. SAVE MODEL
# =========================================================

joblib.dump(
    model,
    "model.pkl"
)


# =========================================================
# 17. SAVE SCALER
# =========================================================

joblib.dump(
    scaler,
    "scaler.pkl"
)


# =========================================================
# 18. SAVE ONE-HOT ENCODER
# =========================================================

joblib.dump(
    ohe,
    "encoder.pkl"
)


# =========================================================
# 19. SAVE EDUCATION ENCODER
# =========================================================

joblib.dump(
    education_encoder,
    "education_encoder.pkl"
)


# =========================================================
# 20. SAVE IMPUTERS
# =========================================================

joblib.dump(
    num_imp,
    "num_imputer.pkl"
)

joblib.dump(
    cat_imp,
    "cat_imputer.pkl"
)


print("\n====================================")
print("MODEL SAVING COMPLETED")
print("====================================")

print("Created files:")

print("model.pkl")
print("scaler.pkl")
print("encoder.pkl")
print("education_encoder.pkl")
print("num_imputer.pkl")
print("cat_imputer.pkl")