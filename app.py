import streamlit as st
import base64

# Set up page
st.set_page_config(page_title="Lavender Blossom Daycare", layout="centered")

# Function to add background
def set_bg(image_file):
    with open(image_file, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            .info-box {{
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 12px;
                margin-top: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Set the background
set_bg("lavender-in-bloom-big-56a5831a3df78cf77288ab2b.jpg")

# Content
st.markdown("<div class='info-box'>", unsafe_allow_html=True)

st.title("🌸 Lavender Blossom Daycare")
st.subheader("A loving and safe place for your child to grow and blossom 🌼")

st.markdown("### 📍 Location")
st.write("13352 SW 157th Ave, Tigard, OR 97223")

st.markdown("### 📞 Contact Us")
st.write("**Phone:** 564-654-1493")
st.write("**Email:** [lavenderblossomdaycare@gmail.com](mailto:lavenderblossomdaycare@gmail.com)")

st.markdown("### 🕕 Hours of Operation")
st.write("**Monday to Friday:** 6:00 AM – 6:00 PM")

st.markdown("### 👶 About Us")
st.write("""
At Lavender Blossom Daycare, we provide a nurturing, creative, and secure environment
where children thrive. Our certified caregivers offer structured learning, fun activities,
and healthy meals throughout the day.

Let your child grow with us — where every little blossom is cared for with love. 🌷
""")

st.markdown("© 2025 Lavender Blossom Daycare")
st.markdown("</div>", unsafe_allow_html=True)
