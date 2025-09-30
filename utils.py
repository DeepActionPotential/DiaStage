import joblib
import pandas as pd

def load_artifacts():
    model = joblib.load("models/random_forest_diabetes_model.pkl")
    scaler = joblib.load("models/age_scaler.pkl")  # scaler used only for AGE
    return model, scaler

def preprocess_input(gender, age, urea, cr, hba1c, chol, tg, hdl, ldl, vldl, bmi):
    data = {
        "Gender": [gender],
        "AGE": [age],
        "Urea": [urea],
        "Cr": [cr],
        "HbA1c": [hba1c],
        "Chol": [chol],
        "TG": [tg],
        "HDL": [hdl],
        "LDL": [ldl],
        "VLDL": [vldl],
        "BMI": [bmi],
    }
    return pd.DataFrame(data)

def predict_stage(model, scaler, features_df):
    # Apply same AGE scaling
    features_df["AGE"] = scaler.transform(features_df[["AGE"]])
    pred = model.predict(features_df)[0]

    # Map numeric class → human readable label
    label_map = {
        0: "Non-diabetic",
        1: "Diabetic",
        2: "Prediabetic"
    }
    return label_map[pred]
