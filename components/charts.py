import streamlit as st
import plotly.express as px
import pandas as pd

def sales_chart(df):
    """Create a sales chart from the provided dataframe."""
    if df.empty:
        st.warning("No data to display")
        return
    
    # Check if the dataframe has the expected columns
    if 'id' in df.columns and 'value' in df.columns:
        fig = px.bar(df, x='id', y='value', title='Sales Data')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Data should have 'id' and 'value' columns")
        st.write("Available columns:", df.columns.tolist())