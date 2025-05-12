import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Lavender Blossom Daycare", layout="centered")

# Load background image and encode to base64
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    page_bg_img = f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function to set background
set_background("background.png")  # Rename your image to 'background.png'

# App content
st.title("🌸 Lavender Blossom Daycare")
st.subheader("A loving and safe place for your child to grow and blossom 🌼")

# Contact info
st.markdown("### 📍 Location")
st.write("13352 SW 157th Ave, Tigard, OR 97223")

st.markdown("### 📞 Contact Us")
st.write("**Phone:** 564-654-1493")
st.write("**Email:** [lavenderblossomdaycare@gmail.com](mailto:lavenderblossomdaycare@gmail.com)")

st.markdown("### 🕕 Hours of Operation")
st.write("**Monday to Friday:** 6:00 AM – 6:00 PM")

# About section
st.markdown("---")
st.markdown("### 👶 About Us")
st.write("""
At Lavender Blossom Daycare, we provide a nurturing, creative, and secure environment
where children thrive. Our certified caregivers offer structured learning, fun activities,
and healthy meals throughout the day.

Let your child grow with us — where every little blossom is cared for with love. 🌷
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Lavender Blossom Daycare")
