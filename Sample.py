import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("salaries.csv")
st.line_chart(df)
st.area_chart(df)
st.scatter_chart
