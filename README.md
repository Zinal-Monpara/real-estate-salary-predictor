# 🏠 Real Estate Salary Predictor

This is a simple Streamlit web app that predicts a person’s salary based on their **years of experience** and **age** using a **Linear Regression** model. The project is organized in VS Code and deployed on **Streamlit Cloud**.

---

## 📦 How to Run the App Locally

To run this app on your computer, follow these steps:

```bash
pip install streamlit pandas scikit-learn joblib
streamlit run app/app.py
```

---

## 📁 Project Files and Folders

```
├── app/
│   └── app.py                  # Main Streamlit app code
├── model/
│   ├── predictor.py            # Model loading and prediction functions
│   └── regression_model.pkl    # Saved linear regression model
├── data/
│   └── real_estate_data.csv    # Sample dataset used for training
├── requirements.txt            # Python libraries used
└── README.md                   # This file
```

---

## 📊 About the Model

- **Model Type**: Linear Regression  
- **Inputs**:  
  - Years of Experience  
  - Age  
- **Output**: Predicted Salary

The model was trained using a small dataset of real estate job roles and is saved using `joblib`.

---

## 🚀 Deployment Info

- This app can be deployed to **Streamlit Cloud** for easy access online.
- Final live app link:  
  [Live App on Streamlit](https://real-estate-predictor.streamlit.app)

- GitHub Repository link:  
  `https://github.com/your-username/Real_Estate_Predictor_Project`

---

## 👩‍💻 Created By

**Zinal Monpara**  
Built as part of a course project using:  
Streamlit | Python | scikit-learn | Linear Regression
