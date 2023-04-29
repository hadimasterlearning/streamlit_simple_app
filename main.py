import streamlit as st
import pandas as pd
import plotly.express as px

raw_data = pd.read_csv(
    "https://bit.ly/50startups_dataset"
)

agg_data = raw_data.groupby('State', as_index=False).size()

bar_fig = px.bar(
    agg_data, x = 'State', y = 'size'
)

st.title("Contoh output berbentuk plot plotly di Streamlit")
st.plotly_chart(bar_fig)
