import streamlit as st
from PIL import Image
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
        }
        .subheader {
            text-align: center;
            font-size: 24px;
            color: #1B4F72;
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
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

st.markdown('<h1 class="title">Certificate Validation System</h1>', unsafe_allow_html=True)
st.write("")
st.markdown('<h2 class="subheader">Select Your Role</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
institite_logo = Image.open("../assets/institute_logo.png")
with col1:
    st.image(institite_logo, output_format="jpg", width=230)
    clicked_institute = st.button("Institute", key="institute_button")

company_logo = Image.open("../assets/company_logo.jpg")
with col2:
    st.image(company_logo, output_format="jpg", width=230)
    clicked_verifier = st.button("Verifier", key="verifier_button")

if clicked_institute:
    st.session_state.profile = "Institute"
    switch_page('login')
elif clicked_verifier:
    st.session_state.profile = "Verifier"
    switch_page('login')