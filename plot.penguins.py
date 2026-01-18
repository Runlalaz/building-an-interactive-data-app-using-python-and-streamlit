import pandas as pd
import plotly.express as px
import streamlit as st


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

##df = pd.read_csv(url)
##df_grouped_by_species = df.groupby("species")["body_mass_g"].mean()
##st.bar_chart(df_grouped_by_species)

# พลอตกราฟด้วย Plotly
##fig = px.bar(df_grouped_by_species.reset_index(), x="species", y="body_mass_g")
##st.plotly_chart(fig)
##df_grouped = df.groupby("sex")["body_mass_g"].mean()
##st.bar_chart(df_grouped)
with st.sidebar:
    st.write("This is a sidebar")
    option = st.selectbox(
        "Which sex?",
        ["MALE","FEMALE"]
    )
    st.write(option)
df = pd.read_csv(url)
df_output = df[df["sex"] == option]
st.write(df_output)