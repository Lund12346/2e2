import streamlit as st
import base64

# Simple Encryption Function (XOR based for demo)
def encrypt_decrypt(string, key):
    result = ""
    for i in range(len(string)):
        char = string[i]
        key_char = key[i % len(key)]
        result += chr(ord(char) ^ ord(key_char))
    return result

# Page Design
st.set_page_config(page_title="My Private Server", page_icon="🔐")
st.title("🛡️ My Secure Offline Server")
st.markdown("---")

# User Input
name = st.text_input("Admin:", "Aapka Naam") 

st.write(f"Hello **{name}**, welcome to your private space.")

mode = st.radio("Choose Mode:", ["Encrypt", "Decrypt"])
message = st.text_area("Message Likhein:")
key = st.text_input("Security Key (Password):", type="password")

if st.button("Process"):
    if message and key:
        if mode == "Encrypt":
            res = encrypt_decrypt(message, key)
            encoded = base64.b64encode(res.encode()).decode()
            st.success("Encrypted Message:")
            st.code(encoded)
        else:
            try:
                decoded = base64.b64decode(message).decode()
                res = encrypt_decrypt(decoded, key)
                st.info("Original Message:")
                st.write(res)
            except:
                st.error("Invalid input ya wrong key!")
    else:
        st.warning("Please enter both message and key.")

