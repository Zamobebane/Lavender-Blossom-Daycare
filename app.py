import streamlit as st

st.set_page_config(page_title="Lavender Blossom Daycare", layout="centered")

# Header
st.title("🌸 Lavender Blossom Daycare")
st.subheader("A loving and safe place for your child to grow and blossom 🌼")

# Location and Contact Info
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

# Image (optional)
st.image("https://images.unsplash.com/photo-1609831194203-5df9db976b5c", caption="A Place to Learn and Bloom", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("© 2025 Lavender Blossom Daycare")
