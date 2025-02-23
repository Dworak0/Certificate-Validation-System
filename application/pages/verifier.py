import streamlit as st
import hashlib
from utils.streamlit_utils import view_certificate
from connection import contract
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

options = ("View/Verify Certificate using Certificate ID",)
selected = st.selectbox("", options, label_visibility="hidden")

if selected == options[0]:
    form = st.form("Validate-Certificate")
    certificate_id = form.text_input("Enter the Certificate ID")
    submit = form.form_submit_button("Validate")
    if submit:
        try:
            view_certificate(certificate_id)
            # Smart Contract Call
            result = contract.functions.isVerified(certificate_id).call()
            if result:
                st.success("Certificate validated successfully!")
            else:
                st.error("Invalid Certificate ID!")
        except Exception as e:
            st.error("Invalid Certificate ID!")
