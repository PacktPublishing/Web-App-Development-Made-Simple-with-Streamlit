import streamlit as st

# Sharing variables between pages
from app import my_variable
from pages.page2 import my_variable_page2

st.subheader("Page1")
st.write(my_variable)
st.write(my_variable_page2)

