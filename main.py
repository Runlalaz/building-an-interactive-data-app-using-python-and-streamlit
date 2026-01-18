import pandas as pd
import streamlit as st


df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
st.write(df)