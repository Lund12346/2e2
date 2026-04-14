import streamlit as st

# Page layout setup
st.set_page_config(page_title="E2EE OFFLINE SERVER", layout="centered")

# Custom CSS for "Same to Same" Look
st.markdown("""
    <style>
    /* Background and Font */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://wallpaperaccess.com/full/416568.jpg");
        background-size: cover;
    }
    
    /* Main Card Design */
    .main-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        color: white;
    }

    /* Input Field */
    .stTextInput input {
        background-color: rgba(0,0,0,0.5) !important;
        color: #00ff00 !important;
        border: 1px solid #444 !important;
    }

    /* Button Style */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px #ff416c;
    }
    </style>
    """, unsafe_allow_html=True)

# UI Elements
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("🛡️ DEVIL SERVER")
st.write("OFFLINE E2EE MULTI-ACCOUNT SYSTEM")

# Input field
appstate = st.text_area("PASTE YOUR APPSTATE / TOKEN HERE", height=150)

# Submit Button
if st.button("START BOT"):
    if appstate:
        st.success("Connection Established! Processing...")
    else:
        st.warning("Please enter valid data first.")

st.markdown('</div>', unsafe_allow_html=True)
