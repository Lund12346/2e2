import streamlit as st
import base64

def encrypt_decrypt(string, key):
    result = ""
    for i in range(len(string)):
        char = string[i]
        key_char = key[i % len(key)]
        result += chr(ord(char) ^ ord(key_char))
    return result

st.set_page_config(page_title="Addie Private Server", page_icon="🛡️")
st.title("🛡️ Addie's Secure Server")

mode = st.radio("Mode Select Karein:", ["Encrypt", "Decrypt"])
message = st.text_area("Message ya Code yahan dalein:")
key = st.text_input("Password dalein:", type="password")

if st.button("Process"):
    if message and key:
        if mode == "Encrypt":
            res = encrypt_decrypt(message, key)
            # Isse error nahi aayega
            encoded = base64.b64encode(res.encode('utf-8')).decode('utf-8')
            st.success("Aapka Encrypted Code:")
            st.code(encoded)
        else:
            try:
                # Decoding logic with error handling
                decoded_bytes = base64.b64decode(message.encode('utf-8'))
                decoded_str = decoded_bytes.decode('utf-8')
                final_res = encrypt_decrypt(decoded_str, key)
                st.info("Original Message:")
                st.write(final_res)
            except Exception:
                st.error("Invalid Input! Shayad code galat hai ya password.")
    else:
        st.warning("Message aur Password dono zaroori hain!")
