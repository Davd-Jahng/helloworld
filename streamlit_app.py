import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello", type="primary"):
    st.write("Why hello there")
else:
    st.write("Goodbye")