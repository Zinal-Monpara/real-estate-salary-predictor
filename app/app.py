
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from model.predictor import load_model, predict

def main():
    st.title("Real Estate Salary Predictor")

    experience = st.slider("Years of Experience", 0, 50, 10)
    age = st.slider("Age", 18, 70, 30)

    if st.button("Predict Salary"):
        try:
            model = load_model()
            salary = predict(model, experience, age)
            st.success(f"Predicted Salary: ${salary}k")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    main()
