import streamlit as st
from utils.data_loader import load_data
from components.charts import sales_chart

st.set_page_config(page_title="My Streamlit App", layout="wide")

st.title("My Streamlit App")

