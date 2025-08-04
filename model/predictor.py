
import joblib
import pandas as pd

def load_model():
    return joblib.load("model/regression_model.pkl")

def predict(model, experience, age):
    input_df = pd.DataFrame([[experience, age]], columns=["Experience", "Age"])
    return round(model.predict(input_df)[0], 2)
