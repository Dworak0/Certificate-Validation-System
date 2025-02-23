import streamlit as st
from db.firebase_app import login
from dotenv import load_dotenv
import os
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

# Set up the page
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

# Load environment variables
load_dotenv()

# Ensure session state variables are initialized
if "profile" not in st.session_state:
    st.session_state.profile = None  # Default value, change as needed

st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
        }
        .stTextInput>div>div>input {
            border: 2px solid #2874A6;
            border-radius: 5px;
            padding: 8px;
        }
        .stButton>button {
            width: 100%;
            background-color: #2874A6;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #1B4F72;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">Login Page</h1>', unsafe_allow_html=True)

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")

if st.session_state.profile != "Institute":
    clicked_register = st.button("New user? Click here to register!")
    if clicked_register:
        switch_page("register")

submit = form.form_submit_button("Login")
if submit:
    if st.session_state.profile == "Institute":
        valid_email = os.getenv("institute_email")
        valid_pass = os.getenv("institute_password")
        if email == valid_email and password == valid_pass:
            switch_page("institute")
        else:
            st.error("Invalid credentials!")
    else:
        result = login(email, password)
        if result == "success":
            st.success("Login successful!")
            switch_page("verifier")
        else:
            st.error("Invalid credentials!")
