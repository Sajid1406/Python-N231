import streamlit as st

st.header("CV :')")
name = st.text_input("Name")
age = st.number_input("Age")
st.write("Name:",name)
st.write("Age:",age)

st.subheader("Package")
st.code("import pandas")