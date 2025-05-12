import streamlit as st
from streamlit.components.v1 import html

# Page Configuration
st.set_page_config(page_title="Lavender Blossom Daycare", page_icon="🌸", layout="centered")

# Custom CSS for Child-Friendly Styling
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .main {
            background-color: #fff0f5;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #6a5acd;
            font-family: "Comic Sans MS", cursive, sans-serif;
        }
        p, div, label {
            font-family: "Comic Sans MS", cursive, sans-serif;
            font-size: 18px;
        }
        .stTextInput > div > div > input {
            background-color: #fffafc;
        }
        .stButton>button {
            background-color: #ffc0cb;
            color: black;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🌸 Lavender Blossom Daycare 🌸</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #ff69b4;'>Where Little Blossoms Bloom with Love</h4>", unsafe_allow_html=True)

# --- Image Banner ---
st.image("https://cdn.pixabay.com/photo/2017/08/10/07/32/children-2616844_1280.jpg", use_column_width=True)

# --- Contact Info Card ---
with st.container():
    st.subheader("📍 Contact Information")
    st.markdown("""
    - **Location:** 13352 SW 157th Ave, Tigard, OR 97223  
    - **Phone:** 📞 [564-654-1493](tel:5646541493)  
    - **Email:** 📧 [lavenderblossomdaycare@gmail.com](mailto:lavenderblossomdaycare@gmail.com)  
    - **Hours:** 🕕 Monday to Friday | 6:00 AM – 6:00 PM
    """)

# --- Mission Section ---
with st.container():
    st.subheader("🎯 Our Mission")
    st.write("""
    At **Lavender Blossom Daycare**, we provide a warm, safe, and creative learning environment for infants and toddlers.
    We focus on emotional growth, hands-on learning, and joyful playtime.

    🌈 Every child is unique, and we are here to nurture their curiosity, creativity, and confidence!
    """)

# --- Inquiry Form ---
with st.container():
    st.subheader("💬 Get in Touch")
    st.write("Have a question? Want to schedule a visit? We'd love to hear from you!")

    with st.form("contact_form"):
        name = st.text_input("Your Name 👶")
        email = st.text_input("Your Email 📧")
        message = st.text_area("Your Message ✍️")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("🎉 Thank you! We'll get back to you as soon as possible.")

# --- Footer ---
st.markdown("---")
st.markdown("<center>© 2025 Lavender Blossom Daycare 🌸</center>", unsafe_allow_html=True)
