import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate the basic functionalities of Streamlit.")

st.sidebar.header("User Input Features")
username = st.sidebar.text_input("What is your name ?", "Aman Raikwar")
age = st.sidebar.slider("Select your age", 0,100,28)
favourite_color=st.sidebar.selectbox("What is your favourite colour?",["Blue","Red","Green","Yellow"])

st.header(f"Welcome, {username}!")
st.write(f"You are {age} years old and your favourite colour is {favourite_color}.")

# Displaying Data
st.subheader("Here's some random data :")

# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' % i for i in range(5))

    # columns = []
    # for i in range(5):
    #   columns.append('col %d' % i)
)
st.dataframe(data)

# Checkbox to show/hide content
if st.checkbox("show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# Button to trigger an action
if st.button("Say Hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")