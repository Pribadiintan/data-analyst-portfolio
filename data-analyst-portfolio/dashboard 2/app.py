import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Telco Customer Analytics Dashboard")

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = load_data()
st.write("### Data Preview")
st.dataframe(df.head())

# ======================
# TABS
# ======================
tab1, tab2, tab3, tab4 = st.tabs(["📈 Regression", "👥 Clustering", "⚡ Classification", "📊 Dashboard"])

# ======================
# REGRESSION (Predict MonthlyCharges)
# ======================
with tab1:
    st.subheader("Regression: Predict Monthly Charges")

    # Ambil fitur numerik
    num_cols = ["tenure", "TotalCharges"]
    df_reg = df[num_cols + ["MonthlyCharges"]].dropna()

    X = df_reg[num_cols]
    y = df_reg["MonthlyCharges"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Li
