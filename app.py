import streamlit as st

st.title("GlobalJava Roasters")
st.header("Customer Feedback Form")
st.write("Your input helps us brew a better experience. Please share your thoughts about our coffee and service.")


# Write new code below:
st.write("Did you enjoy your coffee?")
if st.button("Yes!",key="yes_button"):
    st.write("Glad you enjoyed it!")

if st.button("No!",key="no_button"):
    st.write("We're sorry to hear that. We'll strive to improve.")