import streamlit as st
import base64

st.set_page_config(page_title="Lavender Blossom Daycare", layout="centered")

# ---- BACKGROUND IMAGE FUNCTION ----
def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        page_bg = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.65);
            color: #111 !important;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }}
        h1, h2, h3, h4, h5, h6, p, a, span {{
            color: #111 !important;
        }}
        </style>
        """
        st.markdown(page_bg, unsafe_allow_html=True)

# ---- SET BACKGROUND ----
set_bg_from_local("ChatGPT Image May 12, 2025, 02_00_46 PM.png")

# ---- PAGE CONTENT ----
st.title("Lavender Blossom Daycare")
st.subheader("A loving and safe place for your child to grow and blossom 💜🌿")

st.markdown("### 📍 Location")
st.write("13352 SW 157th Ave, Tigard, OR 97223")

st.markdown("### 📞 Contact Us")
st.write("**Phone:** 564-654-1493")
st.write("**Email:** [lavenderblossomdaycare@gmail.com](mailto:lavenderblossomdaycare@gmail.com)")

st.markdown("### 🕕 Hours of Operation")
st.write("**Monday to Friday:** 6:00 AM – 6:00 PM")

st.markdown("---")
st.markdown("### 💜 About Us 🌿")
st.write("""
At Lavender Blossom Daycare, we provide a nurturing, creative, and secure environment
where children thrive. Our certified caregivers offer structured learning, fun activities,
and healthy meals throughout the day.

Let your child grow with us — where every little blossom is cared for with love. 💜🌿
""")

st.markdown("---")
st.markdown("© 2025 Lavender Blossom Daycare")
