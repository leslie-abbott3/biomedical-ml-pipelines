import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Molecular Metrics Dashboard")

df = pd.read_csv("data/processed/features.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Binding Affinity Distribution")
fig, ax = plt.subplots()
sns.histplot(df["binding_affinity"], bins=30, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), cmap="coolwarm", annot=False, ax=ax)
st.pyplot(fig)
