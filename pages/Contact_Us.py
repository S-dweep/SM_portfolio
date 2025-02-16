import streamlit as st
from send_email import sendEmail

st.header("Contact Me")

with st.form(key="eforms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Message received!!

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        sendEmail(message)
        st.info("Message sent successfully.")