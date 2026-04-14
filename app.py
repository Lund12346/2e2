import streamlit as st

# Page Configuration
st.set_page_config(page_title="E2EE Server", page_icon="🛡️", layout="centered")

# Custom CSS for Design
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# UI Elements
st.title("🛡️ E2EE Offline Server")
st.write("Apna access token niche enter karein:")

token = st.text_input("Enter Access Token", type="password")
if st.button("Submit"):
    if token:
        st.success("Token submitted successfully!")
    else:
        st.error("Please enter a valid token.")
