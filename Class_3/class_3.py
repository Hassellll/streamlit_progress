import streamlit as st 
import pandas as pd

st.title("3rd Class")

st.write("## H2")
st.metric(label="Wind Speed", value="120m/s", delta="1.4 m/s")
tabel = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7,8,9], "column 2": [10,20,30,40,50,60,70,80,90]})
st.table(tabel)
st.dataframe(tabel)
