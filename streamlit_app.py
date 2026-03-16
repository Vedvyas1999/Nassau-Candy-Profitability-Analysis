
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Nassau Candy Profitability Dashboard")

uploaded_file = st.file_uploader("Upload Nassau Candy Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df = df[df['Sales'] > 0]
    df = df[df['Gross Profit'] >= 0]
    df['Units'] = df['Units'].fillna(1)

    df['Gross Margin %'] = (df['Gross Profit'] / df['Sales']) * 100
    df['Profit per Unit'] = df['Gross Profit'] / df['Units']

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Division Performance")
    division = df.groupby("Division")[["Sales","Gross Profit"]].sum()
    st.bar_chart(division)

    st.subheader("Top Profitable Products")
    top_products = df.groupby("Product Name")["Gross Profit"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_products)

    st.subheader("Cost vs Sales")
    fig, ax = plt.subplots()
    ax.scatter(df["Cost"], df["Sales"])
    ax.set_xlabel("Cost")
    ax.set_ylabel("Sales")
    ax.set_title("Cost vs Sales")
    st.pyplot(fig)
