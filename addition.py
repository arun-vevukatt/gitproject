import streamlit as st
st.title("CALCULATOR")
num1=st.number_input("enter first number: ",min_value=0)
num2=st.number_input("enter second number: ",min_value=0)

btn=button("add")
if btn:

    st.write("total: ",num1 + num2)