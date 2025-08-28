# In order to run this file, type in the terminal:
# streamlit run /Users/sparshpatel/bootcamp_sparsh_patel/homework/homework12/streamlit/streamlit_app.py
#change to your relative path

import streamlit as st
import pandas as pd
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# === Load Data ===
data = pd.DataFrame({
    "scenario": ["baseline", "alt_impute", "alt_outlier"],
    "return": [0.12, 0.11, 0.135],
    "volatility": [0.18, 0.185, 0.19],
    "sharpe": [0.56, 0.49, 0.61],
    "assumption": ["imputation", "imputation", "outlier_rule"],
    "value": ["median", "mean", "3sigma"],
    "Category": ["Z", "Y", "X"],
    "MetricA": [58.80, 67.47, 72.47],
    "MetricB": [146.75, 195.34, 170.50],
    "Date": pd.to_datetime(["2025-02-01", "2025-02-02", "2025-02-03"])
})

# === Executive Summary ===
st.title("Scenario Analysis Dashboard")
st.subheader("Executive Summary")
st.write("""
- Baseline delivers a balanced profile (Sharpe ~0.56).  
- Alt-impute lowers risk-adjusted return (Sharpe ~0.49).  
- Alt-outlier shows strongest Sharpe (0.61) but with higher volatility.  
""")

# === Visualizations ===
st.subheader("Visualizations")
col1, col2 = st.columns(2)

# --- Bar chart: Return by Scenario ---
with col1:
    plt.figure(figsize=(5, 4))
    sns.barplot(data=data, x="scenario", y="return", palette="Set2")
    plt.title("Return by Scenario")
    st.pyplot(plt.gcf())
    plt.clf()

# --- Scatter: Risk-Return Tradeoff ---
with col2:
    plt.figure(figsize=(5, 4))
    sns.scatterplot(data=data, x="volatility", y="return", hue="scenario", size="sharpe",
                    sizes=(100, 300), palette="Set2", legend="full")
    for i, row in data.iterrows():
        plt.text(row['volatility'], row['return'] +
                 0.002, row['scenario'], ha='center')
    plt.title("Risk-Return Tradeoff")
    st.pyplot(plt.gcf())
    plt.clf()

# --- Line chart: MetricB over Time ---
plt.figure(figsize=(8, 4))
sns.lineplot(data=data, x="Date", y="MetricB",
             hue="scenario", marker="o", palette="Set2")
plt.title("MetricB over Time")
plt.ylabel("MetricB")
st.pyplot(plt.gcf())
plt.clf()

# === Assumptions & Risks ===
st.subheader("Assumptions & Risks")
st.write("""
- **Baseline** assumes median imputation of missing data.  
- **Alt-impute** assumes mean imputation, which can distort if outliers exist.  
- **Alt-outlier** removes >3σ outliers, improving Sharpe but risking data loss.  

*Risks*: Overfitting scenario choice to historical noise, limited sample size, and assumption-driven bias.
""")

# === Sensitivity Analysis ===
st.subheader("Sensitivity Analysis")
selected = st.selectbox("Choose scenario to stress-test",
                        data["scenario"].unique())

base_row = data[data["scenario"] == "baseline"].iloc[0]
sel_row = data[data["scenario"] == selected].iloc[0]

st.write(f"Comparing **Baseline** vs **{selected}**:")
st.write(f"- Return: {base_row['return']:.3f} → {sel_row['return']:.3f}")
st.write(
    f"- Volatility: {base_row['volatility']:.3f} → {sel_row['volatility']:.3f}")
st.write(f"- Sharpe: {base_row['sharpe']:.3f} → {sel_row['sharpe']:.3f}")

# === Decision Implications ===
st.subheader("Decision Implications")
st.write("""
- If you prefer **stability**, baseline is safest.  
- If you want **higher Sharpe**, outlier-adjusted scenario looks best.  
- Mean imputation underperforms and may be less reliable.  

➡️ **Recommendation**: Consider using outlier-adjusted data but validate robustness with larger samples.
""")